=====================
django-simple-redirects
=====================

.. image:: https://github.com/matthiask/django-simple-redirects/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/matthiask/django-simple-redirects/
    :alt: CI Status

``django.contrib.redirects`` without a ``django.contrib.sites`` dependency

Usage:
======

- Add ``simple_redirects`` to ``INSTALLED_APPS``
- Migrate
- Add ``simple_redirects.middleware.RedirectFallbackMiddleware`` to
  ``MIDDLEWARE_CLASSES``

.. image:: https://travis-ci.org/feinheit/django-simple-redirects.svg?branch=master
    :target: https://travis-ci.org/feinheit/django-simple-redirects
