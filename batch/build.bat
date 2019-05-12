REM Initialize the variables, including the version number.
CALL config.bat

REM Build the package.
CD %build_scripts%
CALL activate base
CALL conda build --py 3.6 --croot "%build_dir%" "%repo_dir%\recipe"
CALL conda build purge

PAUSE