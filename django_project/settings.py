"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from environs import Env
from os import environ
import json
import dj_database_url

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if "SECRETS" in environ:
    secrets = json.loads(environ.get("SECRETS"))
    db_url = secrets["DATABASE_URL"]
    DATABASES = {"default": dj_database_url.parse(db_url)}
    DEBUG = bool(int(secrets["DEBUG"]))
else:
    DATABASES = {"default": dj_database_url.parse("sqlite:///db.sqlite3")}
    DEBUG = True

ALLOWED_HOSTS = ["localhost", ".awsapprunner.com", "rankinglists.net"]
CSRF_TRUSTED_ORIGINS = ['https://*.awsapprunner.com','https://*.127.0.0.1', "https://rankinglists.net/*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django_extensions",
    'crispy_forms',
    "crispy_bootstrap5",
    'captcha',
    "verify_email.apps.VerifyEmailConfig",
    "accounts.apps.AccountsConfig",
    "lists.apps.ListsConfig",
    "list_items.apps.ListItemsConfig",
    "social.apps.SocialConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "django_project.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"] 
STATIC_ROOT = BASE_DIR / "staticfiles" 

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"

DJANGO_SUPERUSER_PASSWORD = env.str("DJANGO_SUPERUSER_PASSWORD") 
DJANGO_SUPERUSER_USERNAME = env.str("DJANGO_SUPERUSER_USERNAME")
DJANGO_SUPERUSER_EMAIL = env.str("DJANGO_SUPERUSER_EMAIL")

RECAPTCHA_PUBLIC_KEY = env.str("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env.str("RECAPTCHA_PRIVATE_KEY")
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_REDIRECT_URL = "lists-entry"
LOGOUT_REDIRECT_URL = "login"
LOGIN_URL = "login"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtppro.zoho.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER') 
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL")

HTML_MESSAGE_TEMPLATE = "registration/email_verification/html_template.html"
VERIFICATION_SUCCESS_TEMPLATE = "registration/email_verification/success.html"
VERIFICATION_FAILED_TEMPLATE = "registration/email_verification/failed.html"
REQUEST_NEW_EMAIL_TEMPLATE = "registration/email_verification/email.html"
LINK_EXPIRED_TEMPLATE = 'registration/email_verification/expired.html'
NEW_EMAIL_SENT_TEMPLATE  = 'registration/email_verification/new_email_sent.html'
SUBJECT = 'Ranking Lists email verification'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}