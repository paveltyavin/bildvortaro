#!/bin/bash
set -e
DJANGO_SETTINGS_MODULE=main.settings.local

source /home/vinograd19/vortaro/env/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

test -d /home/vinograd19/vortaro/pids/ || mkdir -p /home/vinograd19/vortaro/pids/
test -d /home/vinograd19/vortaro/log/ || mkdir -p /home/vinograd19/vortaro/log/

exec gunicorn \
    --env DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE proj.wsgi \
    --bind=localhost:8004 \
    --workers=3 \
    --pid=/home/vinograd19/vortaro/pids/gunicorn_prod.pid \
    --log-file=/home/vinograd19/vortaro/log/gunicorn.log \
    --timeout=600 \
    --user=vinograd19 \
    --group=vinograd19 \
    --log-level=info