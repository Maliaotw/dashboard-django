from .base import *  # noqa
import dj_database_url

MIDDLEWARE.append('django.middleware.security.SecurityMiddleware')
MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')


