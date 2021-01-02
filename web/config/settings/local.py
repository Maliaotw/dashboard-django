from .base import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        "NAME": str(APPS_DIR / "db.sqlite3"),
    }
}