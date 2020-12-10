#!/bin/bash
set -e

echo "Let the DB start.."
sleep 2;

echo "Run migrations"
flask db upgrade
