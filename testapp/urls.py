from django import http
from django.conf.urls import url


urlpatterns = [
    url(r'^something-else/$', lambda request: http.HttpResponse('Hello')),
    url(r'', lambda request: http.HttpResponse('Not found', status=404)),
]
