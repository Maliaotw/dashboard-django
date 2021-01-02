from .base import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': f'django.db.backends.postgresql',
        'NAME': CONFIG.POSTGRES_DB,
        'HOST': CONFIG.POSTGRES_HOST,
        'PORT': CONFIG.POSTGRES_PORT,
        'USER': CONFIG.POSTGRES_USER,
        'PASSWORD': CONFIG.POSTGRES_PASSWORD,
    }
}