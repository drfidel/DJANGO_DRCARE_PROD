from .base import *

DEBUG = False

ADMINS = [
    ('Akiyo Fidel', 'akiyofidel@gmail.com')
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
        
}

TIME_ZONE = 'Africa/Kampala'