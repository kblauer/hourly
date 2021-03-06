"""
Django settings for hourly project.  Created by Kyle Blauer

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# Import the staticfiles directory (/static/)
from django.conf.global_settings import STATICFILES_DIRS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Enable app-specific templates, so that each app has it's own modular template directory
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*0**6n@@omnd-1vc$dxnnyoh!hj+m&e9z!vg5^liq-z9qt*$ap'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'userprofile',
    'schedentry',
    'schedule',
    'contact',
    'comments',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hourly.urls'

WSGI_APPLICATION = 'hourly.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# This sets the user profile app for Django's built in user system.  
# It allows us to create an arbitrary model which extends the information.
# This line creates a 1-to-1 link between a User and a UserProfile
AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

EMAIL_HOST = 'mail.server312.com'
EMAIL_HOST_USER = 'noreply@texasibiz.net'
EMAIL_HOST_PASSWORD = 'viper11'
DEFAULT_FROM_EMAIL = 'noreply@texasibiz.net'
SERVER_EMAIL = 'noreply@texasibiz.net'
EMAIL_USE_TLS = True
EMAIL_PORT = 587