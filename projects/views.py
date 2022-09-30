import re
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

def projects(request):
    proyectos=models.Proyecto.objects.all()
    return render(request, 'projects.html', {'proyectos':proyectos})

@login_required(login_url='login')
def project(request):
    return render(request, 'single-project.html')

def signup(request):
    if request.method == 'POST':    
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
    # Verifica si existe
        if User.objects.filter(username=username).exists():
            return HttpResponse("Error:El nombre de usuario ya existe")
        elif User.objects.filter(email=email).exists():
            return HttpResponse("Error:El correo ya existe")
        else:  
        #crea el usuario
            user=User()
            user.is_active=1
            user.username = username
            user.set_password(password)
            user.email = email
            user.first_name = firstname
            user.last_name = lastname
            user.save()
        #return redirect('app:login')
    return render(request, 'signup.html')


#class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

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
            #messages.error(request, 'Username does not exist')
            return HttpResponse("Error: el usuario no existe")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            #print('Username OR password is incorrect')
            #messages.error(request, 'Username OR password is incorrect')
            return HttpResponse("Error: Usuario o contraseña incorrecta")
            #success_message = "Username OR password"
    return render(request, 'login.html')

def mainPage(request):
    return render(request, 'main.html')

def logoutUser(request):
    logout(request)
    #success_message = "IT was sucesfully logout"
    #messages.error(request, 'User was sucesfully logout')
    return HttpResponse("Logout Correcto")
    return redirect('login')
