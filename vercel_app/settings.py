
from pathlib import Path
import pymysql
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()


# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] if DEBUG else ['wedding-arahmat-project.scale.web.id','.vercel.app', '.now.sh']

SECRET_KEY = os.environ.get('SECRET_KEY')


INTERNAL_IPS = [
    "127.0.0.1",
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django.contrib.staticfiles',
    
    'tailwind',
    'theme',
    # 'django_browser_reload',
    'UserMessage',
    

]

TAILWIND_APP_NAME = 'theme'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # "whitenoise.middleware.WhiteNoiseMiddleware",

    # 'django_browser_reload.middleware.BrowserReloadMiddleware',


    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vercel_app.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vercel_app.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
MEDIA_URL = '/media/'

# if DEBUG:
#     STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
# else:
#     STATIC_ROOT =  BASE_DIR / "staticfiles"

STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'