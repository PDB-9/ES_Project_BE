"""
Django settings for ES_Project project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=p7t(lbl27d-n23nhveq_8o=hp*49owy!(fa&77v_8kxt8jd&x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_elasticsearch_dsl',
    'django_elasticsearch_dsl_drf',
    'django_logging',
    # Project apps
    'spotify',
    'logger'
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django_logging.middleware.DjangoLoggingMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'https://fcpai8781z:rpb78t2zu0@jasmine-450285335.us-east-1.bonsaisearch.net:443'
        # 'hosts': 'localhost:9200'
    },
}
DJANGO_LOGGING = {
    "CONSOLE_LOG": False,
# "ELASTICSEARCH_ENABLED" : True,
    "LOG_PATH": '{}/staticfiles/logs'.format(BASE_DIR),
    "ELASTICSEARCH_ENABLED" : False,
    "LOG_LEVEL": "INFO",
    "RESPONSE_FIELDS" :('content'),
    "IGNORED_PATHS" : ['/admin', '/static', '/favicon.ico', '/log']

}
# LOGGING = {
#     # ...
#     'handlers': {
#         # ...
#         'logstash': {
#             'level': 'INFO',
#             'class': 'logstash.TCPLogstashHandler',
#             'port': 5000,
#             'host': '0.0.0.0', # IP/Name of the EC2 instance,
#             'version': 1,
#             'message_type': 'logstash',
#             'fqdn': True,
#             'tags': ['meetnotes'],
#         },
#     },
#     'logger': {
#         # ...
#         'app_name': {
#             # file will accept only ERROR and higher level
#             'handlers': ['file', 'logstash'],
#             'level': DEBUG,
#         },
#     },
# }


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
    'DATETIME_INPUT_FORMATS': ("%Y-%m-%d %H:%M:%S",),
}

ROOT_URLCONF = 'ES_Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ES_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
