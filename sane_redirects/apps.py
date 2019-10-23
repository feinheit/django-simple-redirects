from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SaneRedirectsConfig(AppConfig):
    name = "sane_redirects"
    verbose_name = _("redirects")
