## ArcGIS Python Environment Setup

Configure an ArcGIS Python environment to include GeoPandas and Rasterio before trying the Python scripts. You can add GeoPandas, Rasterio, and other packages to a base ArcGIS Python environment with the [Deep Learning Libraries Installers for ArcGIS](https://github.com/Esri/deep-learning-frameworks) or create a new environment. If you want to create a new Python environment through ArcGIS Pro:

1. **Clone the base environment**\
Settings &rarr; Package Manager &rarr; Enviornment Manager &rarr; Clone arcgispro-py3 &rarr; Save the enviornment to ..\ESRI\conda\envs\arcgispro-py3-clone or ..\anaconda3\envs

![](/Scripts/ArcGIS_Env_Setup/Clone_Env.png)

You can also clone the environment with the Anaconda command prompt, but use the arcgispro-py3 path for your installation.   
```
conda create --name arcgis_pro --clone C:\Users\brekc\AppData\Local\Programs\ArcGIS\Pro\bin\Python\envs\arcgispro-py3 --pinned
```

2. **Add packages to the cloned environment**\
Activate the cloned environment &rarr; Add Packages &rarr; Add Fiona, Geopandas, and Rasterio


![](/Scripts/ArcGIS_Env_Setup/Add_Packages.png)


With the command prompt, you will 'conda activate' the cloned environment and install from the Esri channel (conda install -c esri) 
```
conda env list
```

```
conda activate arcgis_pro
```

```
conda install -c esri fiona geopandas rasterio
```

2. **Open the Python scripts (.py)**

If you are working with an IDE, set the Python interpreter of the target environment:

**[Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial):** View &rarr; Command Palette &rarr; Python: Select Interpreter

![](/Scripts/ArcGIS_Env_Setup/VS_Code_Python_Interp.png)


**[Pycharm Community](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#):** Settings &rarr; Project &rarr; Python Interpreter &rarr; Add Python Interpreter
> [!NOTE]
> You will need to create a project for '..\No_License_Required-Zonal_Statistics_With_GeoPandas\Scripts'.

![](/Scripts/ArcGIS_Env_Setup/PyCharm_Python_Interp.png)

![](/Scripts/ArcGIS_Env_Setup/PyCharm_Python_Interp_2.png)

**[Spyder]([https://code.visualstudio.com/docs/python/python-tutorial](https://docs.spyder-ide.org/current/faq.html)):** Preferences &rarr; Python Interpreter

![](/Scripts/ArcGIS_Env_Setup/Spyder_Python_Interp.png)


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
