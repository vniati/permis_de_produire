from django.conf.urls import url
from views import register, server, login, user, animateur

urlpatterns = [
    url(r'^$', register),
    url(r'^server$', server),
    url(r'^login$', login),
    url(r'^user$', user),
    url(r'^animateur$', animateur),

]
