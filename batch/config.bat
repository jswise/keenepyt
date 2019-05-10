ECHO OFF

SET version_number=0.0.0
ECHO Version number: %version_number%

SET downloads_dir=%UserProfile%\Downloads

REM Set the location of the code.
FOR %%a IN ("%~dp0\..\..\..") DO SET nearc_dir=%%~fa
echo %nearc_dir%
SET repo_dir=%nearc_dir%\code\keenepyt

REM REM Build the package in the default location.
SET build_scripts=%nearc_dir%\conda\Scripts
SET build_dir=%nearc_dir%\conda\conda-bld

REM REM Define the package's file name using the version number.
SET file_name=keenepyt-%version_number%-py36_0.tar.bz2

REM REM Define the conda Scripts directory, which depends on how things are installed.
SET pro_scripts=C:\Program Files\ArcGIS\Pro\bin\Python\Scripts
SET conda_arcgis_user=%UserProfile%\AppData\Local\Programs\ArcGIS\Pro\bin\Python\Scripts
IF EXIST %conda_arcgis_user% SET pro_scripts=%conda_arcgis_user%
ECHO ArcGIS Scripts folder: %pro_scripts%

REM REM Define the user's environments directory, which also depends on how things are installed.
REM REM SET envs_dir=%UserProfile%\AppData\Local\Programs\ArcGIS\Pro\bin\Python\envs
REM SET envs_dir=%UserProfile%\AppData\Local\ESRI\conda\envs
REM REM SET envs_dir=%UserProfile%\AppData\Local\Continuum\miniconda3\envs

REM FOR %%a IN ("%~dp0\..") DO SET repo_dir=%%~fa

REM Define channel directories (folders).
REM REM SET dev_channel=\\phqWFS03\GISShare\conda\dev
REM REM SET test_channel=\\phqWFS03\GISShare\conda\test
SET prod_channel=%nearc_dir%\channel

ECHO ON
