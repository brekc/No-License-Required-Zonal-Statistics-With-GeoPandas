## Setup Recommendations

Anaconda is a distribution of Python and other languages that provides tools for environment management. [Install](https://www.anaconda.com/) Anaconda, then follow the instructions below:

1. **Clone the repository**

Open Anaconda command prompt or terminal and install git:

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
