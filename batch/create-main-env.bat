REM Initialize the variables, including folder paths.
CALL config.bat

REM REM Create the environment where we'll use the package.
CALL %scripts_dir%\conda create -n main --clone arcgispro-py3 -y

REM REM Add the deployment channel where the package will be.
CALL %scripts_dir%\conda config --env --add channels %build_dir%

PAUSE
