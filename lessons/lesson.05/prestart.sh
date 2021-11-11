#!/usr/bin/env bash

echo Run migrations

python manage.py migrate

echo Run app

exec "$@"
