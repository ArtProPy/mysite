#!/bin/sh
echo "TEST"

set +x

python3 manage.py migrate

apt-get install uwsgi-plugin-python3
uwsgi --http :8000 --module mysite.wsgi

#python3 manage.py runserver
