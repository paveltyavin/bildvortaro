#!/usr/bin/python
from fabric.api import run, env, cd
from fabric.context_managers import prefix

env.use_ssh_config = True

password_prefix = prefix('source /home/vinograd19/vortaro/conf/passwords.sh')


def host_type():
    run('uname -s')
    return


def pull():
    with cd('/home/vinograd19/vortaro/src/'):
        run('git pull -q')
    return


def bower():
    with cd('/home/vinograd19/vortaro/src'):
        run('bower install -s')


def less():
    with cd('/home/vinograd19/vortaro/src'):
        run('lessc -x -s /home/vinograd19/vortaro/src/less/style.less /home/vinograd19/vortaro/extra-static/less/css/style.css')


def migrate():
    with password_prefix:
        with cd('/home/vinograd19/vortaro/src/vortaro'):
            run('./manage_prod.py migrate --noinput')
    return


def collectstatic():
    with password_prefix:
        with cd('/home/vinograd19/vortaro/src/vortaro'):
            run('./manage_prod.py collectstatic --noinput')
    return


def restart():
    run('sudo supervisorctl restart vortaro')


def update():
    pull()
    migrate()
    bower()
    less()
    collectstatic()
    restart()
    return