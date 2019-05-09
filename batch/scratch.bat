setlocal
REM SET parent=%~dp0
FOR %%a IN ("%~dp0\..") DO SET repo_dir=%%~fa
ECHO repo_dir=%repo_dir%