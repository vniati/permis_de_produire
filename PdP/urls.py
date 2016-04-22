from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from registration.backends.simple.views import RegistrationView
from forms import MyRegistrationForm
from views import server

urlpatterns = [
url(r'^$', RegistrationView.as_view(form_class = MyRegistrationForm), name='registration_register'),
url(r'^accounts/', include('registration.auth_urls')),
url(r'^server$', server),
]
