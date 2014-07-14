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
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vortaro',
        'USER': 'vortaro',
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': '127.0.0.1',
        'PORT': '',
    },
}

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN', ''),
}

STATIC_ROOT = '/static/vortaro/static/'
MEDIA_ROOT = '/static/vortaro/media/'

TEMPLATE_DIRS += (
    os.path.abspath(os.path.join(SRC_ROOT, 'templates')),
)