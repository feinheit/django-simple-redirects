=======================
django-simple-redirects
=======================

.. image:: https://github.com/feinheit/django-simple-redirects/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/feinheit/django-simple-redirects/
    :alt: CI Status

``django.contrib.redirects`` without a ``django.contrib.sites`` dependency.

Usage:
======

- Add ``simple_redirects`` to ``INSTALLED_APPS``
- Run ``./manage.py migrate``
- Add ``simple_redirects.middleware.RedirectFallbackMiddleware`` to
  ``MIDDLEWARE``
