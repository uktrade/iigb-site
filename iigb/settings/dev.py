from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = ["127.0.0.1"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r#dy$#jw_1-ny14190b^#$c#l@f*)=l(j^td%u!=60sfqo+ui9'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if DEBUG:
    for app in ["debug_toolbar", "django_extensions"]:
        try:
            __import__(app)
            INSTALLED_APPS.append(app)
        except ImportError:
            pass

if "debug_toolbar" in INSTALLED_APPS:
    MIDDLEWARE.extend([
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ])

try:
    from .local import *
except ImportError:
    pass
