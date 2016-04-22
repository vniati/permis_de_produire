from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from models import GreenEq, RedEq, YellowEq, BlueEq, Rattrapage, DysStandard, DysCritique


def server(request):
    return render(request, "server.html")

def user(request):
    return render(request, "user.html")

def animateur(request):
    return render(request, "animateur.html")
