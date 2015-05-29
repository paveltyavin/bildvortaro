# -*- coding: utf-8 -*-

import os, sys
from django.conf import global_settings

DJANGO_ROOT = os.path.abspath(os.path.join(__file__, '../../../'))
PROJECT_ROOT = os.path.dirname(DJANGO_ROOT)

SECRET_KEY = '123'

ROOT_URLCONF = 'main.urls'

WSGI_APPLICATION = 'main.wsgi.application'

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
    os.path.join(DJANGO_ROOT, 'frontend/public'),
)

TEMPLATE_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
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
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
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

    'django_extensions',

    'app',

    # 3rd-party
    'sorl.thumbnail',
    'rest_framework',
    'social.apps.django_app.default',
)
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'app.context_processors.base',
)

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

AUTH_USER_MODEL = 'app.User'

DEBUG = True
TEMPLATE_DEBUG = True

VK_APP_ID = os.environ.get('VK_APP_ID')
VK_API_SECRET = os.environ.get('VK_API_SECRET')

FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
FACEBOOK_API_SECRET = os.environ.get('FACEBOOK_API_SECRET')

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/'

THUMBNAIL_ENGINE = 'app.pil_engine.Engine'
