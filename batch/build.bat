REM Initialize the variables, including the version number.
CALL config.bat

REM Build the package.
CALL "%build_scripts%\conda" build --croot "%build_dir%" "%repo_dir%\recipe"

PAUSE