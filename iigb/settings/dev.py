from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = ["127.0.0.1"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r#dy$#jw_1-ny14190b^#$c#l@f*)=l(j^td%u!=60sfqo+ui9'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


def add_optional_app(app, on_installed=None):
    """
    :param app: App to add if importable
    :param on_installed: function to call if import succeeded
    """
    try:
        __import__(app)
        INSTALLED_APPS.append(app)
        if on_installed is not None:
            on_installed()
    except ImportError:
        pass


if DEBUG:
    add_optional_app("debug_toolbar", lambda: MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware'))
    add_optional_app("django_extensions")

try:
    from .local import *
except ImportError:
    pass
