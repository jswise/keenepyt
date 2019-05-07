REM Initialize the variables, including folder paths.
CALL config.bat

REM Create the environment where we'll write the code.
CALL %scripts_dir%\conda create -n keene --clone arcgispro-py3 -y
CALL %scripts_dir%\activate %1

REM Install a couple packages to help with development.
CALL %scripts_dir%\conda install -y pylint
CALL %scripts_dir%\conda install -y pyyaml

REM REM Add a path file so Python can find the code.
CALL %scripts_dir%\conda develop %repo_dir%\src

REM REM Create the environment where we'll test the package.
CALL %scripts_dir%\conda create -n localtest --clone arcgispro-py3 -y

REM REM Add the build channel where the package will be.
CALL %scripts_dir%\conda config --env --add channels %build_dir%

REM REM Create the environment where we'll use the package.
CALL %scripts_dir%\conda create -n main --clone arcgispro-py3 -y

REM REM Add the deployment channel where the package will be.
CALL %scripts_dir%\conda config --env --add channels %build_dir%

PAUSE
