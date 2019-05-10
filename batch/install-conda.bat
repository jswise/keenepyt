CALL config.bat
ECHO ON

REM %downloads_dir%\Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /NoRegistry=1 /S /D=%nearc_dir%\conda
CD %nearc_dir%\conda\Scripts
CALL activate root
CALL conda install -c msys2 m2-patch -y
CALL conda install conda-build -y

PAUSE