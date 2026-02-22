#!/bin/bash

# Exit on error
set -e

echo "Building project..."
# Use python3 instead of python3.12 to be safer with paths
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

echo "Build complete."
