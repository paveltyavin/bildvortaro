#!/usr/bin/python
from fabric.api import run, env, cd
from fabric.context_managers import prefix

env.use_ssh_config = True

password_prefix = prefix('source /home/vinograd19/vortaro/conf/passwords.sh')


def host_type():
    run('uname -s')
    return


def pull(hash=None):
    with cd('/home/vinograd19/vortaro/src/'):
        if hash is None:
            run('git pull -q')
    return


def bower():
    with cd('/home/vinograd19/vortaro/src'):
        run('bower install -s')


def less():
    with cd('/home/vinograd19/vortaro/src'):
        run('lessc -x -s /home/vinograd19/vortaro/src/less/style.less /home/vinograd19/vortaro/less_compiled/style.css')


def migrate():
    with password_prefix:
        with cd('/home/vinograd19/vortaro/src/vortaro'):
            run('./manage_prod.py migrate --noinput')
    return

'sudo supervisorctl restart vortaro'

def update(hash=None):
    pull(hash=hash)
    migrate()
    bower()
    less()
    return