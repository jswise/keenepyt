REM Initialize the variables, including the version number.
CALL config.bat

REM Copy from the build directory to the channel directory.
copy %build_dir%\win-64\%file_name% "%dev_channel%\win-64\%file_name%"

REM Index the channel.
"%scripts_dir%\conda" index ""%dev_channel%"

REM Pause so that people running this from Windows Explorer can see it.
PAUSE