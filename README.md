
# No License Required - Zonal Statistics With GeoPandas 

**Brek Chiles, 2025**

## Introduction

  GeoPandas is a geospatial Python library that combines Pandas and Shapely utilities to manipulate geometric and tabular data. Extending the default ArcGIS Python 3 environment with Esri’s Deep Learning Libraries Installers or creating custom Python environments allows users to leverage GeoPandas and other open-source packages in their work. In this repository, I present Python code that builds a zonal statistics tool with GeoPandas and Rasterio. We will examine slope grades of main roadways in Central Redmond, WA, to apply the zonal statistics tool and explore the data analysis and manipulation capabilities of Geopandas. Rasterstats is another Python module offering a standalone zonal statistics tool. I used the zonal statistics tool from Rasterstats to compare results and validate the effectiveness of the GeoPandas-Rasterio zonal statistics tool. Modifying the input options between the GeoPandas-Rasterio and Rasterstats zonal statistics tools yields similar results for both tools. I also provide scripts with examples of implementing the GeoPandas-Rasterio zonal statistics tool with ArcPy and ArcGIS Pro. The repository covers a variety of GIS-Python concepts, and the material is intended for everyone, whether they are new to GIS and Python programming or experienced professionals looking to adopt open-source technologies into their workflows.
  
## Datasets

1. LiDAR DTM data
   - https://lidarportal.dnr.wa.gov/
   - King County West 2021
      
2. City of Redmond, WA, GIS data
   - https://www.redmond.gov/424/Data-Downloads
   - Neighborhood boundaries (https://www.redmond.gov/DocumentCenter/View/40/Neighborhoods-ZIP)
   - Roadway centerlines (https://www.redmond.gov/DocumentCenter/View/31/Street-Centerline-ZIP)
   

## Tools & Packages
1. GDAL/OGR
   - https://gdal.org/
2. GeoPandas
   - https://geopandas.org/
3. Matplotlib
   - https://matplotlib.org/
4. Numpy
   - https://numpy.org/
5. Pandas
   - https://pandas.pydata.org/
6. Rasterio
   - https://rasterio.readthedocs.io/
7. Rasterstats
   - https://pythonhosted.org/rasterstats/
8. Seaborn
   - https://seaborn.pydata.org/
9. Scipy
   - https://scipy.org/

## Setup Recommendations

Anaconda is a distribution of Python and other languages that provides tools for environment management. [Install](https://www.anaconda.com/) Anaconda, then follow the instructions below:

1. Clone the repository and create a new environment
   - Open a command prompt terminal and install git:/n
'''
function git_install(){
  console.log("conda install git");
}
'''
  - 
     
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
