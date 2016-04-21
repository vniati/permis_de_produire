from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from models import GreenEq, RedEq, YellowEq, BlueEq
from forms import RegisterForm
# from forms import RegisterForm
# Create your views here.

def homepage(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            identifiant = register_form.cleaned_data["identifiant"]
            mot_de_passe = register_form.cleaned_data["mot_de_passe"]
            user = User.objects.create(username=identifiant,
                                       password=mot_de_passe)
            user = authenticate(username=identifiant, password=mot_de_passe)
            # user.backend = 'django.contrib.auth.backends.ModelBackend'
            # login(request, user)
            return redirect('/server')
    else:
        register_form = RegisterForm()
    return render(request, "homepage.html",
                          {"form":register_form})

def server(request):
    # user = request.user
    return render(request, "server.html")
