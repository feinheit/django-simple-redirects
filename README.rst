=====================
django-sane-redirects
=====================

``django.contrib.redirects`` without a ``django.contrib.sites`` dependency

Usage:
======

- Add ``sane_redirects`` to ``INSTALLED_APPS``
- Migrate
- Add ``sane_redirects.middleware.RedirectFallbackMiddleware`` to
  ``MIDDLEWARE_CLASSES``

.. image:: https://travis-ci.org/feinheit/django-sane-redirects.svg?branch=master
    :target: https://travis-ci.org/feinheit/django-sane-redirects
