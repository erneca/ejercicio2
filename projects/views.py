from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def projects(request):
    proyectos=models.Proyecto.objects.all()
    return render(request, 'projects.html', {'proyectos':proyectos})

def project(request, pk):
    return render(request, 'single-project.html')

