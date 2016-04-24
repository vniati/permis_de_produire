from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from models import GreenEq, RedEq, YellowEq, BlueEq, Rattrapage, DysStandard, DysCritique

# Djang-registration
from django.contrib.auth import authenticate, get_user_model, login
from registration import signals
from registration.views import RegistrationView as BaseRegistrationView

User = get_user_model()

class RegistrationView(BaseRegistrationView):

    def register(self, form):
        new_user = form.save()
        new_user = authenticate(
            username=getattr(new_user, User.USERNAME_FIELD),
            password=form.cleaned_data['password1']
        )
        login(self.request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        return new_user

    def get_success_url(self, user):
        return '/user'

# =================================================================

def server(request):
    return render(request, "server.html")

def user(request):
    return render(request, "user.html")

def animateur(request):
    return render(request, "animateur.html")
