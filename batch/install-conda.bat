REM Miniconda2-latest-Windows-x86_64.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /S /D=P:\tools\miniconda2
REM Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /NoRegistry=1
REM CD \Projects\NEARC\conda
REM Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /NoRegistry=1 /S /D=C:\Projects\NEARC\conda
REM CD Scripts
CALL conda activate root
CALL conda install -c msys2 m2-patch -y
CALL conda install conda-build -y