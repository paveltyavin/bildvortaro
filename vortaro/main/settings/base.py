# -*- coding: utf-8 -*-

import os, sys
from django.conf import global_settings

DJANGO_ROOT = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
SRC_ROOT = os.path.dirname(DJANGO_ROOT)
PROJECT_ROOT = os.path.dirname(SRC_ROOT)

SECRET_KEY = 'change_me_in_your_derived_settings'

ROOT_URLCONF = 'vortaro.main.urls'

WSGI_APPLICATION = 'vortaro.main.wsgi.application'

ADMINS = ()
MANAGERS = ()

SITE_ID = 1

USE_TZ = False
USE_I18N = True

USE_L10N = False

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'
DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y H:i:s'
DATE_INPUT_FORMATS = ('%d.%m.%Y',)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'vortaro.main.middlewares.StripWhitespaceMiddleware',
    'vortaro.main.middlewares.RemoveSlashMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    # contrib
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'vortaro.app',

    # 3rd-party
    'south',
)
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

# AUTH_USER_MODEL = 'app.User'

DEBUG=True