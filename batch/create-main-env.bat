REM Initialize the variables, including folder paths.
CALL config.bat
CD %pro_scripts%

REM REM Create the environment where we'll use the package.
CALL conda create -n main --clone arcgispro-py3 -y
CALL activate main

REM Add the deployment channel where the package will be.
IF NOT EXIST %prod_channel% mkdir %prod_channel%
CALL conda config --env --add channels %prod_channel%

PAUSE
