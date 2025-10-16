"""
 Name:         zonal_statistics_gpd_arcgis_cmd.py

 Purpose:      Calculates zonal statistics from a raster and boundary layer using Arcpy, Geopandas, and Rasterio

 Author:       Brek Chiles (Email-brekchiles@gmail.com, GitHub-brekc)

 Created:      7/14/2025

 Updated:      00/00/0000

 Version:      1.0.0

 Copyright:    (c) 2025 Brek Chiles
"""

import argparse, os
import arcpy
import geopandas as gpd
import numpy as np
import rasterio as rio
from rasterio.mask import mask

# Parse input arguments
parser = argparse.ArgumentParser(description='Calculate zonal statistics from a raster and boundary layer.')

parser.add_argument('-gdb', '--in_gdb', type=str, required=True, help='Path to geodatabase.')
parser.add_argument('-zone', '--in_zone', type=str, required=True, help='Input zones or boundary.')
parser.add_argument('-raster', '--in_raster', type=str, required=True, help='Input raster.')
parser.add_argument('-touched', '--all_touched_arg', type=str, required=True, help='Turn on or off all_touched argument (On or Off).')
parser.add_argument('-output', '--out_feature', type=str, required=True, help='Output feature.')

args = parser.parse_args()

file_gdb = args.in_gdb
zone_boundary = args.in_zone
raster_data = args.in_raster
zonal_stats_out = args.out_feature
touched = args.all_touched_arg

# Convert 'On'/'Off' to boolean for all_touched argument
if touched.lower() == 'on':
    touched_arg = True
elif touched.lower() == 'off':
    touched_arg = False
else:
    raise ValueError("Invalid value for all_touched argument. Use 'On' or 'Off'.")

# Set input paths to allow layers to be added from Catalog or Contents in ArcGIS Pro
def path_edit(input_path):
    if '.gdb' in input_path:
        path_cut = input_path.split('.gdb')[-1].strip(os.sep)
    else:
        path_cut = input_path

    return path_cut

zone_boundary = path_edit(zone_boundary)
raster_data = path_edit(raster_data)

# Path for file geodatabase raster to tif conversion
gdb_raster = file_gdb + os.sep + raster_data
raster_tif_env = file_gdb.replace(file_gdb.split(os.sep)[-1], '')
raster_tif = raster_tif_env + raster_data + '.tif'

# Set GDAL configuration option
from osgeo import gdal
gdal.SetConfigOption("GDAL_MEM_ENABLE_OPEN", "YES")

# Environment Setup
arcpy.env.workspace = raster_tif_env
arcpy.env.overwriteOutput = True

def main():
    try:
        print('Running script...')

        # Convert file geodatabase raster to tiff
        # Rasterio and GDAL versioning differences can cause errors with file geodatabase rasters
        print('Converting file geodatabse raster data to TIFF format...')

        arcpy.conversion.RasterToOtherFormat(gdb_raster, arcpy.env.workspace)

        # Open raster data with rasterio
        print('Opening raster in Rasterio ...')
        raster_rio = rio.open(raster_tif)

        # Create geodataframe(gdf) for zone boundary
        print('Opening zone boundary as a geodataframe...')
        zone_gdf = gpd.read_file(file_gdb, layer=zone_boundary, driver='OpenFileGDB')

        # Function for cell count
        def cell_count(rio_array):
            cells = rio_array.count()
            return cells
        
        # Function for masked arrays
        def masked_array(geom, data=raster_rio):
            raster_masked, raster_masked_transform = mask(dataset=data, shapes=[geom],
                                  crop=True, all_touched=touched_arg, filled= False, indexes=1)
            return raster_masked
        
        # Calculate zonal statistics
        print('Calculating zonal statistics...')
        zone_gdf['cell_count'] = zone_gdf.geometry.apply(masked_array).apply(cell_count)
        zone_gdf['min'] = zone_gdf.geometry.apply(masked_array).apply(np.min)
        zone_gdf['max'] = zone_gdf.geometry.apply(masked_array).apply(np.max)
        zone_gdf['mean'] = zone_gdf.geometry.apply(masked_array).apply(np.mean)
        zone_gdf['std_dev'] = zone_gdf.geometry.apply(masked_array).apply(np.std)
        zone_gdf['variance'] = zone_gdf.geometry.apply(masked_array).apply(np.var)

        # Save zonal statistics gdf to output file
        print('Saving zonal statistics results to file geodatabase...')            
        zone_gdf.to_file(file_gdb, layer=zonal_stats_out, driver='OpenFileGDB')

        # Close the raster file before deleting
        raster_rio.close()

        # Remove all files matching the raster_tif base name (e.g., .tif, .aux.xml, .ovr, etc.)
        base, _ = os.path.splitext(raster_tif)
        for f in os.listdir(os.path.dirname(raster_tif)):
                if f.startswith(os.path.basename(base)):
                    try:
                        os.remove(os.path.join(os.path.dirname(raster_tif), f))
                    except Exception as e:
                        print(f"Could not remove {f}: {e}")

        pass

    except arcpy.ExecuteError:
        # Use GetMessages when running geoprocessing tools
        print(arcpy.GetMessages(2))

    print('Finished running script')

# INITIAL ENTRY POINT FOR SCRIPT
if __name__ == '__main__':
    # Call main function
    main()
    