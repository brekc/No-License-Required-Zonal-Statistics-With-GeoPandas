## ArcGIS Python Environment Setup

Configure an ArcGIS Python environment to include GeoPandas and Rasterio before trying the Python scripts. You can add GeoPandas, Rasterio, and other packages to a base ArcGIS Python environment with the [Deep Learning Libraries Installers for ArcGIS](https://github.com/Esri/deep-learning-frameworks) or create a new environment. If you want to create a new Python environment through ArcGIS Pro:

Setting U+27A1;



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
