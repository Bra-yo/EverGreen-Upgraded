

from pathlib import Path
import os

from django.conf.global_settings import AUTH_USER_MODEL
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

CSRF_TRUSTED_ORIGINS = ['http://localhost:8000']  # Add your domain


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9=n2og@s+%8#cdr=#%5if4qcm21=kq7s%@u%v2ss624vi4_o&e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # ...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'users.apps.UsersConfig',
    'orders.apps.OrdersConfig',
    'payments.apps.PaymentsConfig',
    'properties.apps.PropertiesConfig'

]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',

]

ROOT_URLCONF = 'EverGreenEstates.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'EverGreenEstates.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {

'google': {

'APP': {

'client_id': os.getenv('GOOGLE_CLIENT_ID'),

'secret': os.getenv('GOOGLE_SECRET'),

}

},

'facebook': {

'APP': {

'client_id': os.getenv('FACEBOOK_CLIENT_ID'),

'secret': os.getenv('FACEBOOK_SECRET'),

},

'METHOD': 'oauth2',

'SCOPE': ['email', 'public_profile'],

'AUTH_PARAMS': {'auth_type': 'reauthenticate'},

},

'twitter': {

'APP': {

'client_id': os.getenv('TWITTER_CLIENT_ID'),

'secret': os.getenv('TWITTER_SECRET'),

}

},

# Add Instagram if needed

'instagram': {

'APP': {

'client_id': os.getenv('INSTAGRAM_CLIENT_ID'),

'secret': os.getenv('INSTAGRAM_SECRET'),

}

}

}


# Load environment variables
load_dotenv()

# Use variables in settings
SECRET_KEY = '$*o3ngaqi20068%3ub7(_6lxyddxl+fdz))6eguosli3!cb$^0'  # Use the key you generated
# Payment Configurations
MPESA_CONFIG = {
    'CONSUMER_KEY': os.getenv('MPESA_CONSUMER_KEY'),
    'CONSUMER_SECRET': os.getenv('MPESA_CONSUMER_SECRET'),
    'BUSINESS_SHORTCODE': os.getenv('MPESA_BUSINESS_SHORTCODE'),
    'PASSKEY': os.getenv('MPESA_PASSKEY'),
    'CALLBACK_URL': os.getenv('MPESA_CALLBACK_URL', 'https://yourdomain.com/mpesa-callback')
}

PAYPAL_CONFIG = {
    'CLIENT_ID': os.getenv('PAYPAL_CLIENT_ID'),
    'SECRET': os.getenv('PAYPAL_SECRET'),
    'MODE': os.getenv('PAYPAL_MODE', 'sandbox')
}

BANK_APIS = {
    'KCB': {
        'API_KEY': os.getenv('KCB_API_KEY'),
        'API_SECRET': os.getenv('KCB_API_SECRET')
    },
    'EQUITY': {
        'API_KEY': os.getenv('EQUITY_API_KEY'),
        'API_SECRET': os.getenv('EQUITY_API_SECRET')
    }}

# settings.py

AUTH_USER_MODEL = 'users.Userprofile'


# Configure redirects
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    }
}

SOCIALACCOUNT_FORMS = {}
ACCOUNT_FORMS = {}
ACCOUNT_ADAPTER = 'users.adapters.CustomAccountAdapter'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'users.views': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

# Add to bottom of settings.py:
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'