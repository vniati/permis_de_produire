from django.conf.urls import url
from views import register, server, login

urlpatterns = [
    url(r'^$', register),
    url(r'^server$', server),
    url(r'^login$', login),
]
