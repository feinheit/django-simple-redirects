from django.contrib import admin

from simple_redirects.models import Redirect


admin.site.register(
    Redirect,
    list_display=("old_path", "new_path"),
    search_fields=("old_path", "new_path"),
)
