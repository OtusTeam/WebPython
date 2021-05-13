#!/usr/bin/env sh

echo "Running migrations"
flask db upgrade

exec "$@"
