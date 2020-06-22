#!/bin/sh

echo "Starting postgres..."

while ! nc -z koko-db 5432; do
  sleep 0.1
done

echo "starting postgres....."

python manage.py run -h 0.0.0.0