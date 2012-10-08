from utils import LOCAL
SITE_ID = 1

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': LOCAL('db_prod.sqlite') ,
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

