from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SaneRedirectsConfig(AppConfig):
    name = 'sane_redirects'
    verbose_name = _('redirects')
