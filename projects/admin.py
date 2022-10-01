from django.contrib import admin

# Register your models here.
from .models import Agregar_moneda, Proyecto, Usuario_registrado

admin.site.register (Proyecto)
admin.site.register (Usuario_registrado)
admin.site.register (Agregar_moneda)