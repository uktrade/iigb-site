from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = ["127.0.0.1"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r#dy$#jw_1-ny14190b^#$c#l@f*)=l(j^td%u!=60sfqo+ui9'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    import debug_toolbar
    INSTALLED_APPS.extend([
        'debug_toolbar',
    ])
except ImportError:
    pass

INSTALLED_APPS.append("django_extensions")

MIDDLEWARE.extend([
    'debug_toolbar.middleware.DebugToolbarMiddleware',
])

try:
    from .local import *
except ImportError:
    pass
