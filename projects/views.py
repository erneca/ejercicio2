import re
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def projects(request):
    proyectos=models.Proyecto.objects.all()
    return render(request, 'projects.html', {'proyectos':proyectos})

@login_required(login_url='login')
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
            #print('Username does not exist')
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            #print('Username OR password is incorrect')
            messages.error(request, 'Username OR password is incorrect')
            success_message = "Username OR password"
    return render(request, 'login.html')

def mainPage(request):
    return render(request, 'main.html')

def logoutUser(request):
    logout(request)
    success_message = "IT was sucesfully logout"
    messages.error(request, 'User was sucesfully logout')
    return redirect('login')
