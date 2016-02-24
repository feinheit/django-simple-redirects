from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Redirect(models.Model):
    old_path = models.CharField(
        _('redirect from'),
        max_length=200,
        unique=True,
        help_text=_(
            "This should be an absolute path, excluding the domain"
            " name. Example: '/events/search/'."))
    new_path = models.CharField(
        _('redirect to'),
        max_length=200,
        blank=True,
        help_text=_(
            "This can be either an absolute path (as above) or a"
            " full URL starting with 'http://'."))

    class Meta:
        ordering = ('old_path',)
        verbose_name = _('redirect')
        verbose_name_plural = _('redirects')

    def __str__(self):
        return u"%s ---> %s" % (self.old_path, self.new_path)
