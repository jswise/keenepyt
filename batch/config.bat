SET version_number=0.0.0

REM Build the package in the default location.
SET build_dir=%UserProfile%\AppData\Local\Continuum\miniconda3\conda-bld

REM Build the package in a custom location.
REM SET build_dir=C:\temp\sdk

REM Define the package's file name using the version number.
SET file_name=nearcdemo-%version_number%-py36_0.tar.bz2

REM Define conda directories (folders).
SET scripts_dir=%UserProfile%\AppData\Local\Continuum\miniconda3\Scripts
SET repo_dir=C:\GIS\NEARC\2019_spring\code\NEARCPackageDemo

REM Define channel directories (folders).
SET dev_channel=\\phqWFS03\GISShare\conda\dev
SET test_channel=\\phqWFS03\GISShare\conda\test
SET prod_channel=\\phqWFS03\GISShare\conda\prod
