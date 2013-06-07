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

# Django settings for NDAPortal project.
import djcelery
djcelery.setup_loader()

#This is the broker url.
BROKER_URL = 'django://'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jenkins',
    'author_management',
    'topic_management',
    'meeting_management',
    'schedule_management',
    'user_management',
    'djnotifications',
    'djcelery',
    'kombu.transport.django',
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
    'topic_management.context.get_topic_categories'
)

ROOT_URLCONF = 'PDTtool.urls'

WSGI_APPLICATION = 'PDTtool.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'pdttool_demo',
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
DOMAIN_NAME = "http://192.168.4.153:8000"
# Add a single template directory in the base dir.
#       This is used for all the apps.
TEMPLATE_DIRS = {
    # The template path for all of the notifications
    #       in the meeting management.
    os.path.join(BASE_DIR, "meeting_management/email_templates"),
    # The template directory in the base directory.
    os.path.join(BASE_DIR, "templates_old"),
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
DEFAULT_FROM_EMAIL = 'the.pdt.portal@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
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
#This is the coverage of the excluded folders.
COVERAGE_EXCLUDES_FOLDERS = ['/topic_management/migrations/*']
#These are the categories that topics fit into.
TOPIC_CATEGORIES = (
    'Proposal',
    'Outline',
    'Workbook',
    'Book',
    'Guest Visit',
    'Opens',
)
NOTIFICATION_DELIMETER = "|||:::|||"
#These are the notification sets.
NOTIFICATION_SETS = {
    "main_set":{
                "varname":"main",
                "title":"Global Notification Settings",
                "order":0
               },
    "countdown_set":{
                "varname":"countdown",
                "title":"Topic Due Date Notifications",
                "order":1
                },
    "startdate_set":{
                "varname":"startdate",
                "title":"Meeting Start Date Settings",
                "order":2
                }
}
"""
" If you add or remove any of these fields you have to migrate the database,
"       these are dynamically set boolean fields.
"""
NOTIFICATION_FIELDS = {
    'email_notification':{
        "fieldname":"emailnotification",
        "notification_set":NOTIFICATION_SETS['main_set'],
        "arguments":{
            "default":True,
            "help_text":"Turn off all emails to your inbox.",
            "verbose_name":"Turn Off All Email Notifications %s %s" % (
                NOTIFICATION_DELIMETER,
                NOTIFICATION_SETS['main_set']['varname'])
        }
    },
    'start_date_notifications':{
        "fieldname":"startdatenotification",
        "notification_set":NOTIFICATION_SETS['startdate_set'],
        "arguments":{
            "default":True,
            "help_text":"Notifies a user of 1 week, 3 days, 2 days, and 1 day from the start date of a meeting.",
            "verbose_name":"Meeting Start Date Notifications %s %s" % (
                NOTIFICATION_DELIMETER,
                NOTIFICATION_SETS['startdate_set']['varname'])
        }
    },
    'start_date_notification_1week':{
        "fieldname":"startdatenotification_1week",
        "notification_set":NOTIFICATION_SETS['startdate_set'],
        "notification_day_count": "7",
        "arguments":{
            "default":True,
            "help_text":"Notifies a user of 1 week from the start date of a meeting.",
            "verbose_name":"1 Week Meeting Start Notification %s %s" % (
                NOTIFICATION_DELIMETER,
                NOTIFICATION_SETS['startdate_set']['varname'])
        }
    },
    'start_date_notification_3days':{
        "fieldname":"startdatenotification_3days",
        "notification_set":NOTIFICATION_SETS['startdate_set'],
        "notification_day_count": "3",
        "arguments":{
            "default":True,
            "help_text":"Notifies a user of 3 days from the start date of a meeting.",
            "verbose_name":"3 Days Meeting Start Notification %s %s" % (
                NOTIFICATION_DELIMETER,
                NOTIFICATION_SETS['startdate_set']['varname'])
        }
    },
    'start_date_notification_2days':{
        "fieldname":"startdatenotification_2days",
        "notification_set":NOTIFICATION_SETS['startdate_set'],
        "notification_day_count": "2",
        "arguments":{
            "default":True,
            "help_text":"Notifies a user of 2 days from the start date of a meeting.",
            "verbose_name":"2 Days Meeting Start Notification %s %s" % (
                NOTIFICATION_DELIMETER,
                NOTIFICATION_SETS['startdate_set']['varname'])
        }
    },
    'start_date_notification_1day':{
        "fieldname":"startdatenotification_1day",
        "notification_set":NOTIFICATION_SETS['startdate_set'],
        "notification_day_count": "1",
        "arguments":{
            "default":True,
            "help_text":"Notifies a user of 1 day from the start date of a meeting.",
            "verbose_name":"1 Day Meeting Start Notification %s %s" % (
                NOTIFICATION_DELIMETER,
                NOTIFICATION_SETS['startdate_set']['varname'])
        }
    },
    'count_down_notification':{
        "fieldname":"countdownnotification",
        "notification_set":NOTIFICATION_SETS['countdown_set'],
        "arguments":{
            "default":True,
            "help_text":"Notifies a user of 1 week, 3 days, 2 days, and 1 day from the topic submission cut off date of a meeting.",
            "verbose_name":"Topic Cut Off Notifications %s %s" % (
                NOTIFICATION_DELIMETER,
                NOTIFICATION_SETS['countdown_set']['varname'])
        }
    },
    'count_down_notification_1week':{
        "fieldname":"countdownnotification_1week",
        "notification_set":NOTIFICATION_SETS['countdown_set'],
        "notification_day_count": "7",
        "arguments":{
            "default":True,
            "help_text":"Notifies a user of 1 week from the topic submission cut off date of a meeting.",
            "verbose_name":"1 Week To Cut Off Notification %s %s" % (
                NOTIFICATION_DELIMETER,
                NOTIFICATION_SETS['countdown_set']['varname'])
        }
    },
    'count_down_notification_3days':{
        "fieldname":"countdownnotification_3days",
        "notification_set":NOTIFICATION_SETS['countdown_set'],
        "notification_day_count": "3",
        "arguments":{
            "default":True,
            "help_text":"Notifies a user of 3 days from the topic submission cut off date of a meeting.",
            "verbose_name":"3 days To Cut Off Notification %s %s" % (
                NOTIFICATION_DELIMETER,
                NOTIFICATION_SETS['countdown_set']['varname'])
        }
    },
    'count_down_notification_2days':{
        "fieldname":"countdownnotification_2days",
        "notification_set":NOTIFICATION_SETS['countdown_set'],
        "notification_day_count": "2",
        "arguments":{
            "default":True,
            "help_text":"Notifies a user of 2 days from the topic submission cut off date of a meeting.",
            "verbose_name":"2 days To Cut Off Notification %s %s" % (
                NOTIFICATION_DELIMETER,
                NOTIFICATION_SETS['countdown_set']['varname'])
        }
    },
    'count_down_notification_1day':{
        "fieldname":"countdownnotification_1day",
        "notification_set":NOTIFICATION_SETS['countdown_set'],
        "notification_day_count": "1",
        "arguments":{
            "default":True,
            "help_text":"Notifies a user of 1 day from the topic submission cut off date of a meeting.",
            "verbose_name":"1 day To Cut Off Notification %s %s" % (
                NOTIFICATION_DELIMETER,
                NOTIFICATION_SETS['countdown_set']['varname'])
        }
    },
}
"""""""""
" End custom settings.
"""""""""
