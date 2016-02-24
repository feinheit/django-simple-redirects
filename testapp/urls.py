from django import http
from django.conf.urls import url


urlpatterns = [
    url(r'', lambda request: http.HttpResponse('Not found', status=404)),
]
