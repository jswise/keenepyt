SET version_number=0.0.0

REM Build the package in the default location.
SET build_dir=%UserProfile%\AppData\Local\Continuum\miniconda3\conda-bld

REM Build the package in a custom location.
REM SET build_dir=C:\temp\sdk

REM Define the package's file name using the version number.
SET file_name=keenepyt-%version_number%-py36_0.tar.bz2

REM Define the conda Scripts directory, which depends on how things are installed.
REM SET scripts_dir=C:\Program Files\ArcGIS\Pro\bin\Python\Scripts
SET scripts_dir=%UserProfile%\AppData\Local\Programs\ArcGIS\Pro\bin\Python\Scripts
REM SET scripts_dir=%UserProfile%\AppData\Local\Continuum\miniconda3\Scripts

REM Define the user's environments directory, which also depends on how things are installed.
REM SET envs_dir=%UserProfile%\AppData\Local\Programs\ArcGIS\Pro\bin\Python\envs
SET envs_dir=%UserProfile%\AppData\Local\ESRI\conda\envs
REM SET envs_dir=%UserProfile%\AppData\Local\Continuum\miniconda3\envs

SET repo_dir=C:\GIS\NEARC\code\KeenePYT

REM REM Define channel directories (folders).
REM SET dev_channel=\\phqWFS03\GISShare\conda\dev
REM SET test_channel=\\phqWFS03\GISShare\conda\test
REM SET prod_channel=\\phqWFS03\GISShare\conda\prod
