from .base import *  # noqa
import os

os.environ.setdefault("DATABASE_URL", CONFIG.HEROKU_POSTGRESQL_GOLD_URL)

import dj_database_url


MIDDLEWARE.append('django.middleware.security.SecurityMiddleware')
MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

# load database from the DATABASE_URL environment variable
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
