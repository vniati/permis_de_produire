from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from models import GreenEq, RedEq, YellowEq, BlueEq

def server(request):
    return render(request, "server.html")
