"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

gettext = lambda s: s

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

REMOTE_SERVER = False
"""True if application is in production, False if it's in development"""
if REMOTE_SERVER:
    ALLOWED_HOSTS = ('{{ project_name }}.com',)
    """A list of strings representing the host/domain names that this Django site can serve."""
    DEBUG = False
    TEMPLATE_DEBUG = False
    """ True only in development to debug your application"""
else:
    ALLOWED_HOSTS = ('localhost','127.0.0.1')
    """A list of strings representing the host/domain names that this Django site can serve."""
    DEBUG = True
    TEMPLATE_DEBUG = True
    """ True only in development to debug your application"""
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
]

TEMPLATES = (
    'templates'
)

MANAGERS = (("errors", "errors@{{ project_name }}.com"),)

DATABASES = {
    'remote': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'name',#'/path/example.db'. Path to database file if using sqlite3.
        'USER': 'user',                      # Not used with sqlite3.
        'PASSWORD': 'password',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                     # Set to empty string for default. Not used with sqlite3.
    },
    'local': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'name',#os.path.dirname(__file__) + "/../dev.db",#'/path/example.db'. Path to database file if using sqlite3.
        'USER': 'user',                      # Not used with sqlite3.
        'PASSWORD': 'password',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                     # Set to empty string for default. Not used with sqlite3.
    },
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j!7z%+(kog8tqv-%y7ga5a#0i+!mc_436p2u&i_v9uy1@!#^&t'

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if REMOTE_SERVER:
    DATABASES['default'] = DATABASES['remote']
else:
    DATABASES['default'] = DATABASES['local']
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')



ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static'))
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

"""
THE FOLLOWING CODE SHOULD BE DELETED AT FIRST CONFIGURATION
"""
import sys

print(u'Check settings.py and after configuration remove the code at the end of the file. In setting.py check following variable:')
print(u'ALLOWED_HOSTS')
print(u'MANAGERS')
print(u'DATABASES')
print(u'INSTALLED_APPS')
sys.exit(0)