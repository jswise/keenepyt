REM Initialize the variables, including folder paths.
CALL config.bat

REM Create the environment where we'll write the code.
CALL create-env.bat nearcdemo

REM Add a path file so Python can find the code.
CALL conda develop %repo_dir%\src

REM Create the environment where we'll test the package.
CALL create-env.bat localtest

REM Add the build channel where the package will be.
CALL conda config --env --add channels %build_dir%
