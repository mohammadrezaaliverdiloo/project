#!/bin/bash/

python $Home/src/manage.py makemigrations
python $Home/src/manage.py migrate
python $Home/src/manage.py runserver 0.0.0.0:8000