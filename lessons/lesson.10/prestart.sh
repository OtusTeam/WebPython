#!/usr/bin/env bash

echo Run migrations

FLASK_APP=main flask db upgrade

echo migrations ok

exec "$@"
