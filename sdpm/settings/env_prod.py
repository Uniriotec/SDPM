from utils import LOCAL
import dj_database_url
SITE_ID = 1

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = False

DATABASES = {
             'default': dj_database_url.config(default='postgres://localhost')
             }