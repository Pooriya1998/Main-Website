from main_website.settings import *

# Quick-start development setting - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sw4t@-i60=)@*94mcxh#3@ni%62$kqgy=^fy8k6t$a32waa%)('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['cubichive.ir', 'www.cubichive.ir', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Application definition

#INSTALLED_APPS = []

# sites framework
SITE_ID = 2


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

CSRF_COOKIE_SECURE = True