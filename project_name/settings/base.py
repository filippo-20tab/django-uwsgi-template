"""
Django settings for {{ project_name }} project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HOME_DIR = str(Path.home())


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cookielaw',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = '{{ project_name }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': False,
        },
    },
]

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'it'

MODELTRANSLATION_DEFAULT_LANGUAGE = 'it'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# STATIC_ROOT = None  # to use only with collectstatic workflow
STATICFILES_DIRS = (os.path.abspath(os.path.join(BASE_DIR, 'static')),)

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))

# Site

BASE_HOST_URL = '{{ project_name }}.com'
BASE_DOMAIN_URL = f'https://www.{BASE_HOST_URL}'

# SITE_ID = 1

# Managers

MANAGERS = (("errors", "errors@20tab.com"),)
ADMINS = MANAGERS

# Email

DEFAULT_NAME = '{{ project_name }}'
SERVER_EMAIL = f'info@{BASE_HOST_URL}'
DEFAULT_FROM_EMAIL = f'{DEFAULT_NAME} <{SERVER_EMAIL}>'
EMAIL_SUBJECT_PREFIX = f'[{DEFAULT_NAME}] '
EMAIL_USE_LOCALTIME = True

# Languages

# LANGUAGES = (
#     ('it', 'Italiano'),
#     ('en', 'English'),
# )
# LOCALE_PATHS = (os.path.abspath(os.path.join(BASE_DIR, 'locale')),)

# User

# AUTH_USER_MODEL = 'users.User'

# Django Auth Urls

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_ERROR_URL = 'home'
# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'home'


# ASSETS

PACKAGE_FILENAME = 'package.json'
STATIC_DEBUG = False
STATIC_PATH = {True: 'dev', False: 'dist'}

# uWSGI

UWSGI_ACCESS_LOG_BASE_PATH = f'{HOME_DIR}/logs/{{ project_name }}_access-'
