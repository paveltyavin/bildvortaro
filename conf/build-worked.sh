#!/bin/bash

source /home/vinograd19/vortaro/env/bin/activate;

cd /home/vinograd19/vortaro/src;
git reset --hard HEAD;
git pull -q;

pip install -r requirements/prod.txt;

cd /home/vinograd19/vortaro/src/vortaro;
./manage_prod.py migrate --noinput;

cd /home/vinograd19/vortaro/src/static/;
bower install;

cd /home/vinograd19/vortaro/src/vortaro;
./manage_prod.py collectstatic --noinput;

cd /home/vinograd19/vortaro/src/static/;
node ./node_modules/grunt-cli/bin/grunt --revision="v`git rev-parse --short HEAD`" --staticRoot="/static/vortaro/static/" --srcDir="/home/vinograd19/vortaro/src/";

sudo supervisorctl restart vortaro;
deactivate;
