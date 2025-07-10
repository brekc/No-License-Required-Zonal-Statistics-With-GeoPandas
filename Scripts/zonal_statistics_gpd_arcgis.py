"""
 Name:         zonal_statistics_gpd_arcgis.py

 Purpose:      Calculates zonal statistics from a raster and boundary layer using Arcpy, Geopandas, and Rasterio

 Author:       Brek Chiles (Email-brekchiles@gmail.com, GitHub-brekc)

 Created:      6/16/2025

 Updated:      00/00/0000

 Version:      1.0.0

 Copyright:    (c) 2025 Brek Chiles
"""

import arcpy
import pandas as pd
import geopandas as gpd
import rasterio as rio
import numpy as np
from rasterio.mask import mask

# Set GDAL configuration option
from osgeo import gdal
gdal.SetConfigOption("GDAL_MEM_ENABLE_OPEN", "YES")

# Enviornment Setup
arcpy.env.workspace = r'C:\Users\brekc\OneDrive\Documents\ArcGIS\Projects\Road_Slope_Analysis_Education_Hill_Redmond_WA'
arcpy.env.overwriteOutput = True

def main():
    try:
        print('Running script...')

        # File geodatabase path
        file_gdb = r'C:\Users\brekc\OneDrive\Documents\ArcGIS\Projects\Road_Slope_Analysis_Education_Hill_Redmond_WA\Road_Slope_Analysis_Education_Hill_Redmond_WA.gdb'

        # Set input paths
        raster_data = r'C:\Users\brekc\OneDrive\Documents\ArcGIS\Projects\Road_Slope_Analysis_Education_Hill_Redmond_WA\Road_Slope_Analysis_Education_Hill_Redmond_WA.gdb\Redmond_Slope_Perc'
        ras_tif = r'C:\Users\brekc\OneDrive\Documents\ArcGIS\Projects\Road_Slope_Analysis_Education_Hill_Redmond_WA\Redmond_Slope_Perc.tif'

        # Convert file geodatabase raster to tif
        # Rasterio and GDAL versioning differences can cause errors with file geodatabase rasters
        print('Converting file geodatabse raster data to TIF format...')
        # Remove all files matching the raster_tif base name (e.g., .tif, .aux.xml, .ovr, etc.)
        base, _ = os.path.splitext(raster_tif)
        for f in os.listdir(os.path.dirname(raster_tif)):
                if f.startswith(os.path.basename(base)):
                    try:
                        os.remove(os.path.join(os.path.dirname(raster_tif), f))
                    except Exception as e:
                        print(f"Could not remove {f}: {e}")
        arcpy.conversion.RasterToOtherFormat(raster_data, arcpy.env.workspace)

        # Open raster data with rasterio
        print('Opening raster in Rasterio ...')
        raster_rio = rio.open(ras_tif)

        # Create geodataframe(gdf) for zone boundary
        print('Opening zone boundary as a geodataframe...')
        zone_gdf = gpd.read_file(file_gdb, layer='Redmond_Roads', driver='OpenFileGDB')

        # Trim zone gdf to needed fields
        print('Trimming zone geodataframe to needed fields...')
        zone_gdf_trim = zone_gdf[['StreetName', 'FromStreet', 'ToStreet','geometry']].copy()

        # Buffer zone boundary
        # Comment out this section if you do not want to buffer the zone boundary
        print('Buffering zone boundary...')
        buffer_value = 50
        zone_gdf_trim_buff = zone_gdf_trim.copy()
        zone_gdf_trim_buff['geometry'] = zone_gdf_trim_buff.buffer(buffer_value)


        # Function for cell count
        def cell_count(masked_array):
            cells = masked_array.count()
            return cells
        
        # Function for masked arrays
        def masked_array(geom, data=raster_rio, **mask_args):
            raster_masked, raster_masked_transform = mask(dataset=data, shapes=[geom],
                                  crop=True, all_touched=True, filled= False, indexes=1)
            return raster_masked
        
        # Calculate zonal statistics
        print('Calculating zonal statistics...')
        zone_gdf_trim_buff['cell_count'] = zone_gdf_trim_buff.geometry.apply(masked_array).apply(cell_count)
        zone_gdf_trim_buff['min'] = zone_gdf_trim_buff.geometry.apply(masked_array).apply(np.min)
        zone_gdf_trim_buff['max'] = zone_gdf_trim_buff.geometry.apply(masked_array).apply(np.max)
        zone_gdf_trim_buff['mean'] = zone_gdf_trim_buff.geometry.apply(masked_array).apply(np.mean)
        zone_gdf_trim_buff['std_dev'] = zone_gdf_trim_buff.geometry.apply(masked_array).apply(np.std)
        zone_gdf_trim_buff['variance'] = zone_gdf_trim_buff.geometry.apply(masked_array).apply(np.var)

        # Save zonal statistics gdf to output file
        print('Saving zonal statistics results to file geodatabase...')            
        zone_gdf_trim_buff.to_file(file_gdb, layer='Zonal_Statistics_Results', driver='OpenFileGDB')

        pass

    except arcpy.ExecuteError:
        # Use GetMessages when running geoprocessing tools
        print(arcpy.GetMessages(2))

    print('Finished running script')

# INITIAL ENTRY POINT FOR SCRIPT
if __name__ == '__main__':
    # Call main function
    main()
    