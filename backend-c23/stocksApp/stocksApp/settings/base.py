import os
from pathlib import Path

# Modelo user modificado
AUTH_USER_MODEL = 'users.CustomUser'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dm%(fgi=psn=!+qr+kv2na#imeqdve44i!x-z+-i2f2aiev+tn'


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    'rest_framework',
    'corsheaders',
]

LOCAL_APPS = [
    'stocksApp',
    'apps.users',
    'apps.product',
    'apps.sales',
]

INSTALLED_APPS = BASE_APPS + THIRD_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'stocksApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'stocksApp.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directorio donde se recopilarán los archivos estáticos en producción
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'users/static'),  # Carpeta de archivos estáticos en la raíz del proyecto
    os.path.join(BASE_DIR, 'product/static'),  # Carpeta de archivos estáticos en la raíz del proyecto
    os.path.join(BASE_DIR, 'sales/static'),  # Carpeta de archivos estáticos en la raíz del proyecto
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True

#Sessions configuration
#https://docs.djangoproject.com/en/5.1/topics/http/sessions/
SESSION_ENGINE = 'django.contrib.sessions.backends.db' # Usa la base de datos para almacenar sesiones
SESSION_COOKIE_NAME = 'sessionid'  # Nombre de la cookie de sesión
SESSION_COOKIE_AGE = 1209600  # Duración de la cookie de sesión en segundos (2 semanas)
SESSION_COOKIE_SECURE = False  # Cambia a True si usas HTTPS
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # La sesión no expira al cerrar el navegador

