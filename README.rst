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
