from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.http import HttpResponseRedirect
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # Django<1.9
    MiddlewareMixin = object

from .models import Redirect


class RedirectFallbackMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response

        full_path = request.get_full_path()

        r = None
        try:
            r = Redirect.objects.get(old_path=full_path)
        except Redirect.DoesNotExist:
            pass
        if settings.APPEND_SLASH and not request.path.endswith('/'):
            # Try appending a trailing slash.
            path_len = len(request.path)
            full_path = full_path[:path_len] + '/' + full_path[path_len:]
            try:
                r = Redirect.objects.get(old_path=full_path)
            except Redirect.DoesNotExist:
                pass
        if r is not None:
            return HttpResponseRedirect(r.new_path)

        # No redirect was found. Return the response.
        return response
