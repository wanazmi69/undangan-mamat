#!/bin/bash

# Build the project
echo "Building the project..."
export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`
python3.9 -m pip install -r requirements.txt




echo "Make Migration..."
python3.9 manage.py tailwind install
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear