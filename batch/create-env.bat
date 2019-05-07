CALL %scripts_dir%\conda create -n %1 --clone arcgispro-py3 -y
CALL %scripts_dir%\activate %1
CALL %scripts_dir%\conda install -y pylint
CALL %scripts_dir%\conda install -y pyyaml
