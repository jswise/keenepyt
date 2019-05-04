REM Initialize the variables, including folder paths.
CALL config.bat

REM Create the environment where we'll write the code.
CALL create-env.bat keene --clone arcgispro-py3

REM Add a path file so Python can find the code.
CALL %scripts_dir%\conda develop %repo_dir%\src

REM Create the environment where we'll test the package.
CALL create-env.bat localtest --clone arcgispro-py3

REM Create the environment where we'll use the package.
CALL create-env.bat main --clone arcgispro-py3

REM Add the build channel where the package will be.
CALL %scripts_dir%\conda config --env --add channels %build_dir%

PAUSE
