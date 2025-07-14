## ArcGIS Python Environment Setup

Configure an ArcGIS Python environment to include GeoPandas and Rasterio before trying the Python scripts. You can add GeoPandas, Rasterio, and other packages to a default ArcGIS Python environment with the [Deep Learning Libraries Installers for ArcGIS](https://github.com/Esri/deep-learning-frameworks) or create a new environment. If you want to create a new Python environment through ArcGIS Pro:

1. **Clone the base environment**\
Settings &rarr; Package Manager &rarr; Enviornment Manager &rarr; Clone arcgispro-py3 &rarr; Save the enviornment to ..\ESRI\conda\envs or ..\anaconda3\envs

![](/Scripts/ArcGIS_Env_Setup/Clone_Env.png)



2. **Add packages to the cloned environment**\
Activate the cloned environment &rarr; Add Packages &rarr; Add Fiona, Geopandas, and Rasterio


![](/Scripts/ArcGIS_Env_Setup/Add_Packages.png)


With the command prompt, you will 'conda activate' the cloned environment and install from the Esri channel (conda install -c esri) 


You can also clone the environment with the Anaconda command prompt, but use the arcgispro-py3 path for your installation.   

```
conda create --name arcgis_pro --clone C:\Users\brekc\AppData\Local\Programs\ArcGIS\Pro\bin\Python\envs\arcgispro-py3 --pinned
```

```
conda env list
```

```
conda activate arcgis_pro
```

```
conda install -c esri fiona geopandas rasterio
```

3. **Open the Python scripts (.py)**

If you are working with an IDE, set the Python interpreter of the target environment:

**[Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial):** View &rarr; Command Palette &rarr; Python: Select Interpreter

![](/Scripts/ArcGIS_Env_Setup/VS_Code_Python_Interp.png)

**[Pycharm Community](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#):** Settings &rarr; Project &rarr; Python Interpreter &rarr; Add Python Interpreter
> [!NOTE]
> You will need to create a project for ..\No_License_Required-Zonal_Statistics_With_GeoPandas\Scripts.

![](/Scripts/ArcGIS_Env_Setup/PyCharm_Python_Interp.png)

![](/Scripts/ArcGIS_Env_Setup/PyCharm_Python_Interp_2.png)

**[Spyder](https://docs.spyder-ide.org/current/faq.html):** Preferences &rarr; Python Interpreter

![](/Scripts/ArcGIS_Env_Setup/Spyder_Python_Interp.png)

> [!NOTE]
> You can also activate environments and launch IDEs through Anaconda Navigator.

![](/Scripts/ArcGIS_Env_Setup/Conda_Nav_IDEs.png)

4. **Run gdb_setup.py first to test your setup and create the geodatabase needed for the other scripts**
   
## Batch file (.bat) Setup

The zonal_statistics_gpd_arcgis_cmd.py script is an example of how to build command-line tools with [argparse](https://docs.python.org/3/library/argparse.html). Edit zonal_statistics_gpd_arcgis_cmd.txt to include the desired Python interpreter and path to zonal_statistics_gpd_arcgis_cmd.py:

> [!WARNING]
> File paths will vary based on your operating system.

1. **Open zonal_statistics_gpd_arcgis_cmd.txt in a text editor**

![](/Scripts/ArcGIS_Env_Setup/Txt_to_Bat_1.png)

Edit the paths for the Python interpreter and zonal_statistics_gpd_arcgis_cmd.py script.

![](/Scripts/ArcGIS_Env_Setup/Txt_to_Bat_2.png)

![](/Scripts/ArcGIS_Env_Setup/Txt_to_Bat_3.png)
   
3. **Save as batch (.bat) file**

![](/Scripts/ArcGIS_Env_Setup/Txt_to_Bat_4.png)
   
4. **Test by dragging and dropping the batch file into a command prompt or terminal, type -h, then enter to see the help message** 

![](/Scripts/ArcGIS_Env_Setup/CMD_Help.png)

A command for the geodatabase from gdb_setup.py will look like:

```
C:\Users\brekc\No_License_Required-Zonal_Statistics_With_GeoPandas\Scripts\zonal_statistics_gpd_arcgis_cmd.bat -gdb C:\Users\brekc\No_License_Required-Zonal_Statistics_With_GeoPandas\Scripts\zonal_statistics_gpd_arcgis.gdb -zone Redmond_Roads -raster King_Co_2021_Ext_Perc -touched On -output zonal_stats_test
``` 
