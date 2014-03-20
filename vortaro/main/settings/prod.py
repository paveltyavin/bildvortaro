from vortaro.main.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = False
INSTALLED_APPS += ('gunicorn',)

ALLOWED_HOSTS = [
    '*',
]
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(PROJECT_ROOT, 'logs/django.log'),
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['sentry'],
            'propagate': False,
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vortaro',
        'USER': 'vortaro',
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': '',
    },
}

RAVEN_CONFIG = {
    'dsn': 'http://{}@sentry.tyavin.name/2'.format(os.environ['SENTRY_KEY']),
}

STATIC_ROOT = '/static/vortaro/static/'
MEDIA_ROOT = '/static/vortaro/media/'


STATICFILES_DIRS += (
    os.path.join(PROJECT_ROOT, 'less_compiled/'),
)