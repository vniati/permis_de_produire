from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from models import GreenEq, RedEq, YellowEq, BlueEq
from forms import RegisterForm, LoginForm
# from forms import RegisterForm
# Create your views here.

def login(request):
    if request.method == 'POST':
<<<<<<< HEAD
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            identifiant = register_form.cleaned_data["identifiant"]
            mot_de_passe = register_form.cleaned_data["mot_de_passe"]
            user = User.objects.create(username=identifiant,
                                       password=mot_de_passe)
            user = authenticate(username=identifiant, password=mot_de_passe)
            # user.backend = 'django.contrib.auth.backends.ModelBackend'
            # login(request, user)
=======
        # register_form = RegisterForm(request.POST)
        # if register_form.is_valid():
        #     identifiant = register_form.cleaned_data["identifiant"]
        #     password = register_form.cleaned_data["password"]
        #     user = User.objects.create(username=identifiant,
        #                                password=password)
>>>>>>> e20f7f8e6812713a535b100c8dbe4cee622a7bdf
            return redirect('/server')
    else:
        register_form = RegisterForm()
    return render(request, "login.html",
                          {"form":register_form})

def register(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            identifiant = login_form.cleaned_data["identifiant"]
            password = login_form.cleaned_data["password"]
            user = User.objects.create(username=identifiant,
                                       password=password)
            return redirect('/login')
    else:
        login_form = LoginForm()
    return render(request, "register.html",
                          {"form":login_form})

def server(request):
    # user = request.user
    return render(request, "server.html")
