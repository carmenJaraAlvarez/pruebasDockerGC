DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

STATIC_ROOT = '/app/static/'
MEDIA_ROOT = '/app/static/media/'
ALLOWED_HOSTS = ['*']

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

BASEURL = 'http://35.246.81.197'

APIS = {
    'authentication': 'http://35.246.81.197',
    'base': 'http://35.246.81.197',
    'booth': 'http://35.246.81.197',
    'census': 'http://35.246.81.197',
    'mixnet': 'http://35.246.81.197',
    'postproc': 'http://35.246.81.197',
    'store': 'http://35.246.81.197',
    'visualizer': 'http://35.246.81.197',
    'voting': 'http://35.246.81.197',
}
