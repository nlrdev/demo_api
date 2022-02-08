#!/bin/bash

python manage.py makemigrations
python manage.py migrate
gunicorn api.wsgi:application  -b 0.0.0.0:80