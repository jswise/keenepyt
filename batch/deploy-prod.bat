REM Initialize the variables, including the version number.
CALL config.bat

REM Copy from the build directory to the channel directory.
copy %test_channel%\win-64\%file_name% "%prod_channel%\win-64"

REM Index the channel.
"%scripts_dir%\conda" index ""%prod_channel%"

REM Pause so that people running this from Windows Explorer can see it.
PAUSE