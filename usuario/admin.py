from django.contrib import admin
from .models import UsuarioDato
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields= ("creacion","actualizacion")

admin.site.register(UsuarioDato)