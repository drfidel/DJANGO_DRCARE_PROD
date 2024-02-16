from .base import *

DEBUG = os.getenv("DEBUG") == "True"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TIME_ZONE = 'Africa/Kampala'