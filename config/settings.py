"""
Django settings for config project.
"""

from pathlib import Path
import os
import dj_database_url  # Import dj-database-url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# This is the primary BASE_DIR definition
BASE_DIR = Path(__file__).resolve().parent.parent


# --- Production-Ready Settings from Guide ---

# Read SECRET_KEY from environment variable, with a fallback for development
# WARNING: The fallback is insecure and should NOT be used in production
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-l%vdm7hc2p8p5*!)9^$y*q5tje&10g^eem8%$69%8=u%u6we8_')

# Read DEBUG from environment variable. Defaults to 'True' for local dev.
# This line is CORRECT. DO NOT CHANGE IT.
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Read ALLOWED_HOSTS from environment variable.
# Defaults to '127.0.0.1,localhost' for local dev.
# On Render, you will set this to 'your-app-name.onrender.com'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')


# --- Application definition ---

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pyq',  # Your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Whitenoise (Step 5)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Correctly pointing to your new 'templates' folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# --- Database (Step 6) ---
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# Uses dj_database_url to parse the DATABASE_URL environment variable
# Defaults to a local sqlite3 database if DATABASE_URL is not set
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'
    )
}


# --- Password validation ---
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# --- Internationalization ---
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- Static files (CSS, JavaScript, Images) (Step 2 & 5) ---
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
# This is where collectstatic will gather all static files
STATIC_ROOT = BASE_DIR / 'staticfiles'

# This correctly points to your new 'static' folder for JS/CSS
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Whitenoise storage (Step 5)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Media files (User Uploads) (Step 2) ---

MEDIA_URL = '/media/'
# This is where user-uploaded files will be stored locally
MEDIA_ROOT = BASE_DIR / 'media'


# --- Default primary key field type ---
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'