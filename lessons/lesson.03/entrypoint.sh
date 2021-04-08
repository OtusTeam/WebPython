#!/usr/bin/env bash

echo "Running entrypoint in $(pwd)"

#flask db upgrade
echo "Run command: $@"
exec "$@"
