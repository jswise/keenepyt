ECHO OFF

SET version_number=0.0.1
ECHO Version number: %version_number%

SET downloads_dir=%UserProfile%\Downloads

REM Get the location of the code.
FOR %%a IN ("%~dp0\..\..\..") DO SET nearc_dir=%%~fa
echo %nearc_dir%
SET repo_dir=%nearc_dir%\code\keenepyt

REM Build the package in the default location. This will also be the test channel.
SET build_scripts=%nearc_dir%\conda\Scripts
SET build_dir=%nearc_dir%\conda\conda-bld

REM Define the package's file name using the version number.
SET file_name=keenepyt-%version_number%-py36_0.tar.bz2

REM Define the conda Scripts directory, which depends on how things are installed.
SET pro_scripts=C:\Program Files\ArcGIS\Pro\bin\Python\Scripts
SET conda_arcgis_user=%UserProfile%\AppData\Local\Programs\ArcGIS\Pro\bin\Python\Scripts
IF EXIST %conda_arcgis_user% SET pro_scripts=%conda_arcgis_user%
ECHO ArcGIS Scripts folder: %pro_scripts%

REM Get the location of the conda environments.
SET envs_dir=%UserProfile%\AppData\Local\ESRI\conda\envs

REM Define the production channel.
SET prod_channel=%nearc_dir%\channel

ECHO ON
