from django.contrib import admin

# Register your models here.
from .models import Proyecto, Usuario_registrado

admin.site.register (Proyecto)
admin.site.register (Usuario_registrado)