from .base import *

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DEBUG = False
ADMINS = [
    ('Dulmini', 'dulminiguruge@gmail.com'),
]
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bitcoingame',
        'USER': 'bitcoindatabaseuser',
        'PASSWORD': 'F.5Z+cS(u]d<0Rd3',
        # https://console.cloud.google.com/sql/instances
        'HOST': '34.152.31.66',
        'PORT': '5432', #at the moment of this writing google cloud postgresql is using the default postgresql port 5432
        'OPTIONS': {
            'sslmode': 'verify-ca', #leave this line intact
            'sslrootcert': '/code/cryptoclient/cryptoclient/settings/server-ca.pem',
            "sslcert": "/code/cryptoclient/cryptoclient/settings/client-cert.pem",
            "sslkey": "/code/cryptoclient/cryptoclient/settings/client-key.pem",
    },

    
 
    }
}