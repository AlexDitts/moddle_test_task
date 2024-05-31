#!/bin/sh


echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"


python manage.py migrate
python manage.py loaddata fixtures/fixtures.json
python manage.py collectstatic --noinput

exec "$@"