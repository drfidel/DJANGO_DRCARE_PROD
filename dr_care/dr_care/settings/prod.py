from .base import *
import dj_database_url

DEBUG = False

ADMINS = [
    ('Akiyo Fidel', 'akiyofidel@gmail.com')
]

ALLOWED_HOSTS = ['*']

DATABASES = {
        'default': dj_database_url.config(
            default = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3"))
        
}

TIME_ZONE = 'Africa/Kampala'