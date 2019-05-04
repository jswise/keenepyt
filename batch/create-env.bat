CALL %scripts_dir%\conda create -n %1 -y python=3.6.5
CALL %scripts_dir%\conda activate %1
REM CALL %scripts_dir%\conda install -y pandas
REM CALL %scripts_dir%\conda install -y cx_oracle
REM CALL %scripts_dir%\conda install -y pytest
REM CALL %scripts_dir%\conda install -y pylint
REM CALL %scripts_dir%\conda install -y pyyaml
REM CALL %scripts_dir%\conda install -y requests
REM CALL %scripts_dir%\conda install -y sphinx