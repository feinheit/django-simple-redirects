from __future__ import absolute_import, unicode_literals

from coverage import Coverage

cov = Coverage()  # noqa
cov.start()  # noqa


import os
import sys
import django
from django.conf import settings


settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        },
    },
    INSTALLED_APPS=(
        'sane_redirects',
    ),
    SECRET_KEY='tests',
    ROOT_URLCONF='testapp.urls',
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE_CLASSES=(
        'sane_redirects.middleware.RedirectFallbackMiddleware',
    ),
)

django.setup()


def runtests():
    from django.conf import settings
    from django.test.utils import get_runner

    test_runner = get_runner(settings)(verbosity=2, interactive=True)
    failures = test_runner.run_tests([])

    cov.stop()
    cov.report(
        include=['*/sane_redirects/*'],
        omit=['*migrations*'],
    )
    if 'TRAVIS' not in os.environ:
        cov.html_report(
            include=['*/sane_redirects/*'],
            omit=['*migrations*'],
        )
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
