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


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q*$frtad4ncwg7#=@*8s5so+7&w9mlf(2d-p*(*_dd4x4q-3#h'

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
    # Extensions for utility.
    'django_extensions',
    ###
    # This is the main app for IntelPress PDT portal,
    #   it is at the root level in urls.py
    ###
    'dashboard',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'PDTtool.urls'

WSGI_APPLICATION = 'PDTtool.wsgi.application'

TEMPLATE_STRING_IF_INVALID = 'none'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    ###
    # Dashboard context processor, it basically
    #    gets the list of models.
    ###
    'dashboard.context_processors.dashboard.dashboard_models',
    ###
    # Load the search form which is used 
    #   across multiple templates.
    ###
    'dashboard.context_processors.dashboard.search_form',    
)

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'django_db2',
        'USER': 'django_login',
        'PASSWORD': 'Password',
    }
}

#Find the static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    ('downloads','/home/programmer/upload_dir/'),
)

# Set the email SMTP server
EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'the.pdt.portal@gmail.com'

EMAIL_HOST_PASSWORD = 'cummings123'

EMAIL_PORT = 587

#The default login url if not specified.
LOGIN_URL = '/login/'

#tHIS IS THE DEFAULT UPLOAD DIRECTORYS
FILE_UPLOAD_TEMP_DIR = '/TMP'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = '/static/'
