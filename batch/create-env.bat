CALL %scripts_dir%\conda create -n %1 --clone arcgispro-py3 -y
CALL %scripts_dir%\conda activate %1
REM CALL %scripts_dir%\conda install -y pandas
REM CALL %scripts_dir%\conda install -y cx_oracle
REM CALL %scripts_dir%\conda install -y pytest
CALL %scripts_dir%\conda install -y pylint
REM CALL %scripts_dir%\conda install -y pyyaml
REM CALL %scripts_dir%\conda install -y requests
REM CALL %scripts_dir%\conda install -y sphinx