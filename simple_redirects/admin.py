from django.contrib import admin

from .models import Redirect


admin.site.register(Redirect, list_display=("old_path", "new_path"))
