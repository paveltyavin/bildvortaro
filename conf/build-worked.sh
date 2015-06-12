#!/bin/bash
export PRODUCTION="1";
source /home/vinograd19/vortaro/env/bin/activate;

cd /home/vinograd19/vortaro/src;
git reset --hard HEAD;
git pull -q;

pip install -r requirements/base.txt;

cd /home/vinograd19/vortaro/src/;
python manage.py migrate --noinput;

cd /home/vinograd19/vortaro/src/frontend;
nvm use "0.12";
npm install;
gulp;

cd /home/vinograd19/vortaro/src/;
python manage.py collectstatic --noinput;

sudo supervisorctl restart vortaro;
deactivate;
