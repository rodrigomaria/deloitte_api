#! /bin/bash

# turn on bash's job control
set -m
python scripts/wait_for_mysql.py
python manage.py migrate --settings="deloitte_api.settings"

uwsgi --ini uwsgi.ini --py-autoreload=2 --honour-stdin --workers 1 --threads 1
