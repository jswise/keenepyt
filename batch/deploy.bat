REM Initialize the variables, including the version number.
CALL config.bat

REM Copy from the build directory to the channel directory.
IF NOT EXIST %prod_channel%\win-64\ mkdir %prod_channel%\win-64
copy %build_dir%\win-64\%file_name% "%prod_channel%\win-64\%file_name%"

REM Index the channel.
CD %build_scripts%
CALL activate base
conda index "%prod_channel%"

PAUSE