=====================
django-sane-redirects
=====================

.. image:: https://github.com/matthiask/django-sane-redirects/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/matthiask/django-sane-redirects/
    :alt: CI Status

``django.contrib.redirects`` without a ``django.contrib.sites`` dependency

Usage:
======

- Add ``sane_redirects`` to ``INSTALLED_APPS``
- Migrate
- Add ``sane_redirects.middleware.RedirectFallbackMiddleware`` to
  ``MIDDLEWARE_CLASSES``

.. image:: https://travis-ci.org/feinheit/django-sane-redirects.svg?branch=master
    :target: https://travis-ci.org/feinheit/django-sane-redirects
