REM Initialize the variables, including the version number.
CALL config.bat

REM Build the package.
CALL "%scripts_dir%\conda" build --croot "%build_dir%" "%repo_dir%\recipe"

REM Pause so that people running this from Windows Explorer can see it.
PAUSE