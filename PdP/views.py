from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from models import GreenEq, RedEq, YellowEq, BlueEq
# Create your views here.
def homepage(request):
    if request.method == 'GET':
        return render(request, "homepage.html")
    elif request.method == "POST":
        username = request.POST["identhome"]
        password = request.POST["identmdp"]
        user = User.objects.create(username=username,
                                       password=password)
        if user is not None:
            if user.is_active:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
        return redirect("/server")

def server(request):
    user = request.user
    if user.is_authenticated():
        print "oktamer"
    return render(request, "server.html", {"user":user})
