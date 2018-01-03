from ._heroku import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
