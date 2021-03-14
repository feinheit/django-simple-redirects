from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpleRedirectsConfig(AppConfig):
    name = "simple_redirects"
    verbose_name = _("redirects")
