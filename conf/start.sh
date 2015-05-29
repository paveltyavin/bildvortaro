#!/bin/bash
set -e
DJANGODIR=/home/vinograd19/vortaro/src/vortaro
DJANGO_SETTINGS_MODULE=vortaro.main.settings.prod

LOGFILE=/home/vinograd19/vortaro/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=1
# user/group to run as
USER=vinograd19
GROUP=vinograd19
cd /home/vinograd19/vortaro/src/vortaro
source /home/vinograd19/vortaro/env/bin/activate
source /home/vinograd19/vortaro/conf/passwords.sh

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

test -d $LOGDIR || mkdir -p $LOGDIR
exec /home/vinograd19/vortaro/src/vortaro/manage_prod.py run_gunicorn \
    --bind=localhost:8011 \
    --workers=$NUM_WORKERS \
    --pid=/home/vinograd19/vortaro/pids/gunicorn.pid \
    --log-file=$LOGFILE \
    --user=$USER \
    --group=$GROUP \
    --log-level=debug