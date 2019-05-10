REM Initialize the variables, including folder paths.
CALL config.bat
CD %pro_scripts%

REM Create the environment where we'll write the code.
CALL conda create -n dev --clone arcgispro-py3 -y
CALL activate dev
CALL conda install -y pytest
CALL conda install -y pylint

REM REM Add a path file so Python can find the code.
ECHO %repo_dir%\src > %envs_dir%\dev\Lib\site-packages\keenepyt.pth

REM REM Create the environment where we'll test the package.
CALL conda create -n localtest --clone arcgispro-py3 -y

REM REM Add the build channel where the package will be.
CALL activate localtest
CALL conda config --env --add channels %build_dir%

PAUSE
