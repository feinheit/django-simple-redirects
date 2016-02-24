DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    },
}
INSTALLED_APPS = (
    'sane_redirects',
)
SECRET_KEY = 'tests'
ROOT_URLCONF = 'testapp.urls'
ALLOWED_HOSTS = ['*']
MIDDLEWARE_CLASSES = (
    'sane_redirects.middleware.RedirectFallbackMiddleware',
)
