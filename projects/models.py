import email
from unittest.util import _MAX_LENGTH
import uuid
import datetime
from email.policy import default
from enum import unique
from operator import truediv
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Proyecto(models.Model):
    name = models.CharField(max_length=200)
    document = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    def __str__(self):
        return "%s the name" % self.name


class Usuario_registrado(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    #usuario.id = models.Model.ForeignKey(User, on_delete=models.CASCADE)
    document = models.CharField(max_length=200)
    #moneda=models.CharField(max_length=20, choices=monedas, default='1')
    moneda = models.CharField(max_length=200)
    def __str__(self):
        return "%s the user_registered" % self.document

class Agregar_moneda(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    dinero = models.FloatField(max_length=200)
    fecha_carga=models.DateTimeField()
    def __str__(self):
        return "%s the user_registered" % self.dinero

#class Agregar_moneda(models.Model):
#    cedula = models.ForeignKey(Usuario_registrado, on_delete=models.CASCADE)
#    name = models.CharField(max_length=50)

#    def __str__(self):
#        return "%s the waiter at %s" % (self.name, self.restaurant)



#class Proyecto(models.Model):
#    id = models.AutoField(primary_key=True)
#    name = models.CharField(max_length=200)
#    document = models.CharField(max_length=200)
#    email = models.EmailField(null=True, blank=True)

def __str__(self):
    return self.name