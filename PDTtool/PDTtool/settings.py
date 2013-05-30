"""
Django settings for PDTtool project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#Set the project directory.
PROJECT_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9aoc!08j%@dq=xj2lz7=+(ba&x#=lpnldma#pwlx@wlm$)ri8s'

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
    'author_management',
    'topic_management',
    'meeting_management',
    'schedule_management',
    'user_management',
    # Extensions for utility.
    'django_extensions',
    'pdtresources',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    #This context adds the usersgroups
    #       variable to the templates.
    'user_management.context.groups_context',
    'topic_management.context.search_form',
)

ROOT_URLCONF = 'PDTtool.urls'

WSGI_APPLICATION = 'PDTtool.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'test_migration',
        'USER': 'django_login',
        'PASSWORD': 'Password',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Phoenix'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

"""""""""
" These are custom settings.
"""""""""
# Add a single template directory in the base dir.
#       This is used for all the apps.
TEMPLATE_DIRS = {
    # The template directory in the base directory.
    os.path.join(BASE_DIR, "templates"),
}
# Add a single static directory in the base dir.
#       This is used for all the apps.
STATICFILES_DIRS = (
    # The template is in the static directory.
    ('www',os.path.join(BASE_DIR, "www")),
)
# Set the email SMTP server
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'the.pdt.portal@gmail.com'
EMAIL_HOST_PASSWORD = 'cummings123'
EMAIL_PORT = 587
#The default login url if not specified.
LOGIN_URL = '/login/'
#A prefix for the directory where your projects
#   download files will be stored.
TOPIC_PREFIX_DIR = os.path.abspath(os.path.join(PROJECT_DIR, '..','uploaded_topics'))
#This is a custom setting for the
#   upload directory.
UPLOADED_TOPIC_DIR = "%s/uploads" % TOPIC_PREFIX_DIR
#This is a custom setting for the
#   approved directory.
APPROVED_TOPIC_DIR = "%s/approved" % TOPIC_PREFIX_DIR
#This is a custom setting for the
#   approved directory.
DELETED_TOPIC_DIR = "%s/deleted" % TOPIC_PREFIX_DIR
"""""""""
" End custom settings.
"""""""""