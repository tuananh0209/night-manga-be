from .settings import *  # noqa
from .settings import env

DEBUG = env.bool("DEBUG", default=True)

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
