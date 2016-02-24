from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import Redirect


admin.site.register(
    Redirect,
    list_display=('old_path', 'new_path'),
)
