#!/bin/sh

# ถ้ามี error ให้หยุดทำงานทันที
set -e

echo "Applying database migrations..."
python manage.py migrate
python manage.py import_locations

echo "Starting server..."
# รันคำสั่งที่ส่งมาจาก CMD ใน Dockerfile (คือ gunicorn)
exec "$@"