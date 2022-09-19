from django import http
from django.urls import path, re_path


urlpatterns = [
    path("something-else/", lambda request: http.HttpResponse("Hello")),
    re_path(r"", lambda request: http.HttpResponse("Not found", status=404)),
]
