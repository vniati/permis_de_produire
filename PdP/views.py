from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from models import GreenEq, RedEq, YellowEq, BlueEq
from forms import RegisterForm, LoginForm
# from forms import RegisterForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        # register_form = RegisterForm(request.POST)
        # if register_form.is_valid():
        #     identifiant = register_form.cleaned_data["identifiant"]
        #     password = register_form.cleaned_data["password"]
        #     user = User.objects.create(username=identifiant,
        #                                password=password)
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
