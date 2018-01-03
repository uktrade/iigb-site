from .heroku_base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

try:
    from .local import *
except ImportError:
    pass
