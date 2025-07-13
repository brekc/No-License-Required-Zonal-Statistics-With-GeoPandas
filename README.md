
# No License Required - Zonal Statistics With GeoPandas 

**Brek Chiles, 2025**

## Introduction

  GeoPandas is a geospatial Python library that combines Pandas and Shapely utilities to manipulate geometric and tabular data. Extending the default ArcGIS Python 3 environment with Esri’s Deep Learning Libraries Installers or creating custom Python environments allows users to leverage GeoPandas and other open-source packages in their work. In this repository, I present Python code that builds a zonal statistics tool with GeoPandas and Rasterio. We will examine slope grades of main roadways in Central Redmond, WA, to apply the zonal statistics tool and explore the data analysis and manipulation capabilities of Geopandas. Rasterstats is another Python module offering a standalone zonal statistics tool. I used the zonal statistics tool from Rasterstats to compare results and validate the effectiveness of the GeoPandas-Rasterio zonal statistics tool. Modifying the input options between the GeoPandas-Rasterio and Rasterstats zonal statistics tools yields similar results for both tools. I also provide scripts with examples of implementing the GeoPandas-Rasterio zonal statistics tool with ArcPy and ArcGIS Pro. The repository covers a variety of GIS-Python concepts, and the material is intended for everyone, whether they are new to GIS and Python programming or experienced professionals looking to adopt open-source technologies into their workflows.
  
## Datasets

1. LiDAR DTM data
   - [WA DNR - Washington LiDAR Portal](https://lidarportal.dnr.wa.gov/)
   - King County West 2021
      
2. Roadways and neighborhoods of Redmond, WA
   - [City of Redmond, WA, Maps & GIS](https://www.redmond.gov/416/Maps-GIS)
   - [Neighborhood boundaries](https://www.redmond.gov/DocumentCenter/View/40/Neighborhoods-ZIP)
   - [Roadway centerlines](https://www.redmond.gov/DocumentCenter/View/31/Street-Centerline-ZIP)
   

## Tools & Packages
* [GDAL/OGR](https://gdal.org/)
  
* [GeoPandas](https://geopandas.org/)
  
* [Matplotlib](https://matplotlib.org/)
  
* [Numpy](https://numpy.org/)
  
* [Pandas](https://pandas.pydata.org/)
  
* [Rasterio](https://rasterio.readthedocs.io/)
  
* [Rasterstats](https://pythonhosted.org/rasterstats/)
  
* [Seaborn](https://seaborn.pydata.org/)
  
* [Scipy](https://scipy.org/)

## Setup Recommendations

Anaconda is a distribution of Python and other languages that provides tools for environment management. [Install](https://www.anaconda.com/) Anaconda, then follow the instructions below:

1. **Clone the repository**

Open a command prompt terminal and install git:

```
conda install git
```

Use git clone:

```
git clone https://github.com/brekc/No_License_Required-Zonal_Statistics_With_GeoPandas.git
```

2. **Create a new environment**

Change directories to where GIS_Python_Env.yml is located

```
cd No_License_Required-Zonal_Statistics_With_GeoPandas
```

```
cd Setup
```

Create an environment with GIS_Python_Env.yml

```
conda env create -f GIS_Python_Env.yml
```

Activate the environment

```
conda activate GIS_Python_Env
```

3. **Open IPython Notebooks (.ipynb)**

Launch Jupyter Notebook

```
jupyter notebook
```

> [!NOTE]
> You can also launch Jupyter Notebook or Visual Studio Code through Anaconda Navigator. Make sure the kernel is set to the GIS_Python_Env environment.

4. Run all code cells in GDAL_Raster_Priming.ipynb
   - GDAL_Raster_Priming.ipynb will create the additional input files for Geopandas_Zonal_Statistics.ipynb

## Relevant Resources
* Zonal statistics in ArcGIS
   - [How zonal statistics tools work](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/how-zonal-statistics-works.htm)
   - [Zonal Statistics (Spatial Analyst)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/zonal-statistics.htm)
   - [Zonal Statistics as Table (Spatial Analyst)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/zonal-statistics-as-table.htm)
     
* Zonal statistics in ArcGIS
   - [How zonal statistics tools work](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/how-zonal-statistics-works.htm)
   - [Zonal Statistics (Spatial Analyst)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/zonal-statistics.htm)
   - [Zonal Statistics as Table (Spatial Analyst)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/zonal-statistics-as-table.htm)
     
* Slope Classes
   - https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2017JF004494
