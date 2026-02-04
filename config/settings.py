
SECRET_KEY = 'dummy'
DEBUG = True
INSTALLED_APPS = [
 'django.contrib.contenttypes',
 'django.contrib.auth',
 'rest_framework',
 'products',
 'stores',
 'orders',
]
DATABASES = {
 'default': {
   'ENGINE': 'django.db.backends.sqlite3',
   'NAME': 'db.sqlite3',
 }
}
ROOT_URLCONF = 'config.urls'
