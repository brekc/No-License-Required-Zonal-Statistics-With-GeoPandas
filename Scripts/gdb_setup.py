"""
 Name:         gdb_setup.py

 Purpose:      Creates a geodatabase for zonal_statistics_gpd_arcgis.py 

 Author:       Brek Chiles (Email-brekchiles@gmail.com, GitHub-brekc)

 Created:      7/13/2025

 Updated:      00/00/0000

 Version:      1.0.0

 Copyright:    (c) 2025 Brek Chiles
"""

import arcpy
import os

# Setup directory for gdb
gdb_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Current working directory: {gdb_dir}")
repo_dir = gdb_dir.rsplit(os.sep, 1)[0]
print(f"Repository directory: {repo_dir}")

arcpy.env.workspace = gdb_dir
arcpy.env.overwriteOutput = True

def main():
    try:
        print('Running script...')

        # Set file paths
        raster_data_elevation = os.path.join(repo_dir, 'Inputs', 'DEM', 'King_Co_2021_Ext.tif')
        raster_data_slope = os.path.join(repo_dir, 'Inputs', 'DEM', 'King_Co_2021_Ext_Perc.tif')
        neighborhoods_shp = os.path.join(repo_dir, 'Inputs', 'Boundary', 'Redmond_Neighborhoods.shp')
        study_area_shp = os.path.join(repo_dir, 'Inputs', 'Boundary', 'Redmond_Study_Area.shp')
        roads_shp = os.path.join(repo_dir, 'Inputs', 'Roads', 'Redmond_Roads.shp')

        # Create a gdb if it doesn't exist
        gdb_name = "zonal_statistics_gpd_arcgis.gdb"
        gdb_path = os.path.join(gdb_dir, gdb_name)
        if not arcpy.Exists(gdb_path):
            arcpy.CreateFileGDB_management(gdb_dir, gdb_name)
            print(f"Geodatabase created at: {gdb_path}")
        else:
            print(f"Geodatabase already exists at: {gdb_path}")
        
        # Export shapefiles to geodatabase
        arcpy.FeatureClassToGeodatabase_conversion(
            [neighborhoods_shp, study_area_shp, roads_shp], gdb_path
        )
        print("Exported shapefiles to geodatabase...")

        # Export rasters to geodatabase
        arcpy.conversion.RasterToGeodatabase(
            [raster_data_elevation, raster_data_slope], gdb_path
        )
        print("Exported rasters to geodatabase...")

        pass

    except arcpy.ExecuteError:
        # Use GetMessages when running geoprocessing tools
        print(arcpy.GetMessages(2))

    print('Finished running script')


# INITIAL ENTRY POINT FOR SCRIPT
if __name__ == '__main__':
    # Call main function
    main()
