from main_website.settings import *

# Quick-start development setting - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sw4t@-i60=)@*94mcxh#3@ni%62$kqgy=^fy8k6t$a32waa%)('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

'''
INSTALLED_APPS = [
    'debug_toolbar',
]
'''

# sites framework
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


INTERNAL_IPS = [
    '127.0.0.1'
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

# SMTP Configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_POST = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "po.rahimzade00@gmail.com" # An email to send a message
EMAIL_HOST_PASSWORD = "" # Email password

