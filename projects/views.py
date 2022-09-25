import re
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def projects(request):
    proyectos=models.Proyecto.objects.all()
    return render(request, 'projects.html', {'proyectos':proyectos})

def project(request):
    return render(request, 'single-project.html')

def signup(request):
    return render(request, 'signup.html')

def loginUser(request):

    if request.user.is_authenticated:
        return('projects')

    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']

        try:
            user= User.objects.get(username=username)
        except:
            print('Username does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            print('Username OR password is incorrect')
    return render(request, 'login.html')

def mainPage(request):
    return render(request, 'main.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
