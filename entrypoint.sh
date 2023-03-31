#!/bin/bash

cd /app/core

python manage.py migrate

exec "$@"