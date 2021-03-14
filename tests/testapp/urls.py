from django import http
from django.urls import re_path


urlpatterns = [
    re_path(r"^something-else/$", lambda request: http.HttpResponse("Hello")),
    re_path(r"", lambda request: http.HttpResponse("Not found", status=404)),
]
