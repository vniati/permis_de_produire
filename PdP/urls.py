from django.conf.urls import url
from views import homepage, server

urlpatterns = [
    url(r'^$', homepage),
    url(r'^server$', server),
]
