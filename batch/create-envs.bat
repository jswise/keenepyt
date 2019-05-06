REM Initialize the variables, including folder paths.
CALL config.bat

REM Create the environment where we'll write the code.
CALL create-env.bat keene
CALL %scripts_dir%\conda install conda-build -y

REM REM Add a path file so Python can find the code.
REM CALL %scripts_dir%\conda develop %repo_dir%\src

REM REM Create the environment where we'll test the package.
REM CALL create-env.bat localtest --clone arcgispro-py3

REM REM Create the environment where we'll use the package.
CALL create-env.bat main

REM REM Add the build channel where the package will be.
REM CALL %scripts_dir%\conda config --env --add channels %build_dir%

PAUSE
