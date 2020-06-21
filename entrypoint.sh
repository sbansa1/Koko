#!/bin/sh

echo "Starting postgres..."

while ! nc -z db_name port; do
  sleep 0.1
done

echo "starting postgres....."

python manage.py run -h 0.0.0.0