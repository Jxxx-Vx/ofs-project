#!/bin/sh

#Stop if runs into any errors
set -e

#Collect static files
echo "Collect static files."
python manage.py collectstatic --noinput

#Generate SQL commands for preinstalled apps
echo "Apply makemigrations."
python manage.py makemigrations

#Execute SQL commands.
echo "Execute database migrations."
python manage.py migrate

# Start server
python manage.py runserver 0.0.0.0:8000
# uwsgi --socket :8000 --master --enable-threads --module project_settings.wsgi
