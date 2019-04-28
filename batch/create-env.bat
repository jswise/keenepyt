CALL conda create -n %1 -y python=3.6.5
CALL activate %1
CALL conda install -y pandas
CALL conda install -y cx_oracle
CALL conda install -y pytest
CALL conda install -y pylint
CALL conda install -y pyyaml
CALL conda install -y requests
CALL conda install -y sphinx