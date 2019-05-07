SET scripts_dir=%UserProfile%\AppData\Local\Continuum\miniconda3\Scripts
SET conda_arcgis_user=%UserProfile%\AppData\Local\Programs\ArcGIS\Pro\bin\Python\Scripts
SET conda_arcgis_default=C:\Program Files\ArcGIS\Pro\bin\Python\Scripts
IF EXIST %conda_arcgis_user% SET scripts_dir=%conda_arcgis_user%
IF EXIST %conda_arcgis_default% SET scripts_dir=%conda_arcgis_default%

echo %scripts_dir%
