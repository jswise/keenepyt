ECHO OFF

SET version_number=0.0.0
ECHO Version number: %version_number%

SET downloads_dir=%UserProfile%\Downloads

FOR %%a IN ("%~dp0\..\..\..") DO SET nearc_dir=%%~fa
echo %nearc_dir%

REM REM Build the package in the default location.
REM REM setlocal
REM SET build_dir=%UserProfile%\AppData\Local\Continuum\miniconda3\conda-bld

REM REM Build the package in a custom location.
REM REM SET build_dir=C:\temp\keene

REM REM Define the package's file name using the version number.
REM SET file_name=keenepyt-%version_number%-py36_0.tar.bz2

REM REM Define the conda Scripts directory, which depends on how things are installed.
REM SET scripts_dir=%UserProfile%\AppData\Local\Continuum\miniconda3\Scripts
REM SET conda_arcgis_user=%UserProfile%\AppData\Local\Programs\ArcGIS\Pro\bin\Python\Scripts
REM SET conda_arcgis_default=C:\Program Files\ArcGIS\Pro\bin\Python\Scripts
REM IF EXIST %conda_arcgis_user% SET scripts_dir=%conda_arcgis_user%
REM IF EXIST %conda_arcgis_default% SET scripts_dir=%conda_arcgis_default%

REM REM Define the user's environments directory, which also depends on how things are installed.
REM REM SET envs_dir=%UserProfile%\AppData\Local\Programs\ArcGIS\Pro\bin\Python\envs
REM SET envs_dir=%UserProfile%\AppData\Local\ESRI\conda\envs
REM REM SET envs_dir=%UserProfile%\AppData\Local\Continuum\miniconda3\envs

REM FOR %%a IN ("%~dp0\..") DO SET repo_dir=%%~fa

REM REM REM Define channel directories (folders).
REM REM SET dev_channel=\\phqWFS03\GISShare\conda\dev
REM REM SET test_channel=\\phqWFS03\GISShare\conda\test
REM REM SET prod_channel=\\phqWFS03\GISShare\conda\prod
