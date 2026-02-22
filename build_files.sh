#!/bin/bash

# Exit on error
set -e

echo "Building project..."
# Use --break-system-packages to bypass PEP 668 restriction in the build container
python3 -m pip install -r requirements.txt --break-system-packages

echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

echo "Build complete."
