REM Initialize the variables, including the version number.
CALL config.bat

REM Copy from the build directory to the channel directory.
copy %build_dir%\win-64\%file_name% "%prod_channel%\win-64"

REM Index the channel.
"%build_scripts%\conda" index ""%prod_channel%"

PAUSE