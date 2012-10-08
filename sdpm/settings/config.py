
from utils import LOCAL

ADMINS = (
    ('Arruda', 'contato@arruda.blog.br'),
)
MANAGERS = ADMINS

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True

USE_L10N = True


# Login/Logout URL
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'urls'

MEDIA_ROOT = LOCAL('media') 
MEDIA_URL = '/media/'

STATIC_ROOT = LOCAL('static_root')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    LOCAL('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    LOCAL('templates')
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

)

AUTHENTICATION_BACKENDS = ( 
        'user_backends.email_username.EmailOrUsernameModelBackend',
        'django.contrib.auth.backends.ModelBackend',
)
