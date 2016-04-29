from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Djang-registration
from registration.views import RegistrationView as BaseRegistrationView
from django.contrib.auth import authenticate, get_user_model, login
from registration import signals
from models import GreenEq, RedEq, YellowEq, BlueEq, Rattrapage, DysStandard, DysCritique, ColorChoiceForm

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
        return '/server'

# =================================================================


def server(request):
    if request.method == "POST":
        form = ColorChoiceForm(request.POST)
        if form.is_valid():
            post.save()
            return redirect('/user')
    else:
        form = ColorChoiceForm()
    return render(request, "server.html", {'form': form})


@login_required(login_url='/accounts/login/')
def user(request):
    nombre = 4
    carte_standard = DysStandard.objects.order_by('?').first()
    carte_critique = DysCritique.objects.order_by('?').first()
    carte_rattrapage = Rattrapage.objects.order_by('?').first()
    return render(request, "user.html", {"carte_standard":carte_standard, "carte_critique":carte_critique, "carte_rattrapage":carte_rattrapage, "nombre":nombre} )


def animateur(request):
    return render(request, "animateur.html")
