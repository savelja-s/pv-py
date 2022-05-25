#!/bin/bash

source venv/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
deactivate
