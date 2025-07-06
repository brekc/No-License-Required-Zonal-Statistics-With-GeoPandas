
# No License Required - Zonal Statistics With GeoPandas 

**Brek Chiles, 2025**

## Introduction

  GeoPandas is a geospatial Python library that combines Pandas and Shapely utilities to manipulate geometric and tabular data. Extending the default ArcGIS Python 3 environment with Esri’s Deep Learning Libraries Installers or creating custom Python environments allows users to leverage GeoPandas and other open-source packages in their work. In this repository, I present Python code that builds a zonal statistics tool with GeoPandas and Rasterio. We will examine slope grades of main roadways in Central Redmond, WA, to apply the zonal statistics tool and explore the data analysis and manipulation capabilities of Geopandas. Rasterstats is another Python module offering a standalone zonal statistics tool. I used the zonal statistics tool from Rasterstats to compare results and validate the effectiveness of the GeoPandas-Rasterio zonal statistics tool. Modifying the input options between the GeoPandas-Rasterio and Rasterstats zonal statistics tools yields similar results for both tools. I also provide scripts with examples of implementing the GeoPandas-Rasterio zonal statistics tool with ArcPy and ArcGIS Pro. The repository covers a variety of GIS-Python concepts, and the material is intended for everyone, whether they are new to GIS and Python programming or experienced professionals looking to adopt open-source technologies into their workflows.
  
## Datasets

1. LiDAR data for computing topographic slope and CTI inputs
   - https://lidarportal.dnr.wa.gov/
   - Olympics North Opsw 2018, OESF 2014, and Olympic Park 2014
2. 30 M9 CSZ earthquake scenarios for PGV input
   - https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published//PRJ-1355/Frankel_etal_Production/csz010
   - For the NetCDF file, contact Alex Grant (agrant@usgs.gov) 
3. Surface geology at 1:100,000 scale for lithology input
   - https://www.dnr.wa.gov/programs-and-services/geology/publications-and-data/gis-data-and-databases
4. ESA WorldCover for land cover input
   - https://esa-worldcover.org/en

## Tools & Packages
1. Fiona
   - https://pypi.org/project/Fiona/
2. GDAL
   - https://gdal.org/
3. Matplotlib
   - https://matplotlib.org/stable/api/index
4. Numpy
   - https://numpy.org/doc/stable/
5. Pandas
   - https://pandas.pydata.org/docs/
6. Rasterio
   - https://rasterio.readthedocs.io/en/latest/index.html
7. Rioxarray
   - https://corteva.github.io/rioxarray/stable/index.html
8. Scipy
   - https://docs.scipy.org/doc/scipy/
9. Xarray
   - https://docs.xarray.dev/en/stable/

## Methodology
1. Data Collection (Python & QGIS)
   - Geospatial Datasets, Landslide Inventory, Fieldwork (May and July 2021)
2. Calculate Coseismic Landslide Probability (Python)
   - Calculate probability for 30 M9 CSZ scenarios (Frankel et al., 2018)
3. Geospatial Analysis (QGIS)
   - Find overlap between 30 probability models for 50% and 75% probability thresholds, High-risk Area Estimates
4. Sensitivity Analysis for PGV Spatial Resolution (Python)
   - Percent change for high-risk area between 100 m and 50 m probability overlap maps

## Relevant Resources
1. USGS webpage on earthquake-triggered landslides and the Nowicki Jessee et al. (2018) model 
   - https://earthquake.usgs.gov/data/ground-failure/background.php
2. Article on the Nowicki Jessee et al. (2018) model
   - https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2017JF004494
