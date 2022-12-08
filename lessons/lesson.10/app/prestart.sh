#!/usr/bin/env bash

set -e

echo run migrations

flask db upgrade

exec "$@"
