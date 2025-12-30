"""
Django settings for assidu project.
"""
import os
from pathlib import Path

###################################################################################
def get_env_variable(var_name):
    """Get the env var value or throw an exception"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


###################################################################################

# 
RUNNING_DEVSERVER = (get_env_variable("ASSIDU_ACTIVATE_DEV_TOOLS") == "1")
# 
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("ASSIDU_SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

BASE_INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'timezone_field',
    'neapolitan',
    'accounts',
    'assidu',
]

DEV_ONLY_INSTALLED_APPS = [
    'django_extensions',
	#'debug_toolbar',
]

if RUNNING_DEVSERVER:
    INSTALLED_APPS = BASE_INSTALLED_APPS + DEV_ONLY_INSTALLED_APPS
else:
    INSTALLED_APPS = BASE_INSTALLED_APPS

BASE_MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#DEV_ONLY_MIDDLEWARE = (
#    "debug_toolbar.middleware.DebugToolbarMiddleware",
#)
DEV_ONLY_MIDDLEWARE = ()

# NOTE: Putting the DEV_ONLY_MIDDLEWARE first in the resulting
# MIDDLEWARE works for now but might not work for all situations.
if RUNNING_DEVSERVER:
    MIDDLEWARE = DEV_ONLY_MIDDLEWARE + BASE_MIDDLEWARE 
else:
    MIDDLEWARE = BASE_MIDDLEWARE

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, 'templates/'),
            ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
print("A")
print(os.path.join(BASE_DIR, 'templates/'))
print("B")

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'

AUTH_USER_MODEL = 'accounts.User'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

USE_THOUSAND_SEPARATOR=True
