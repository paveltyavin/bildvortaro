from vortaro.main.settings.base import *

INSTALLED_APPS += ('gunicorn',)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {},
    'loggers': {},
}

INSTALLED_APPS += ('django_jenkins',)
JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.with_coverage',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db/1.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    },
}

