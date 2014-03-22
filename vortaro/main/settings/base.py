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

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(SRC_ROOT, 'static')),
    os.path.abspath(os.path.join(PROJECT_ROOT, 'extra-static/less')),
    os.path.abspath(os.path.join(PROJECT_ROOT, 'extra-static/bower')),
)

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(SRC_ROOT, 'templates')),
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
    # 'social_auth.middleware.SocialAuthExceptionMiddleware',
    'vortaro.main.middlewares.StripWhitespaceMiddleware',
    'vortaro.main.middlewares.RemoveSlashMiddleware',
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
    'sorl.thumbnail',
    'social_auth',
    'rest_framework',
)
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'vortaro.app.context_processors.base',
)

AUTH_USER_MODEL = 'app.User'

DEBUG = True
TEMPLATE_DEBUG = True

JENKINS_TASKS = (
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.run_jslint',
    'django_jenkins.tasks.run_csslint',
    'django_jenkins.tasks.run_sloccount',
    'django_jenkins.tasks.lettuce_tests',
)

VK_APP_ID = os.environ.get('VK_APP_ID')
VK_API_SECRET = os.environ.get('VK_API_SECRET')

FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
FACEBOOK_API_SECRET = os.environ.get('FACEBOOK_API_SECRET')

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/'