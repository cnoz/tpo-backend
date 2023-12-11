from django.contrib import admin
from .models import EmpresaDatos
# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    readonly_fields= ("creacion","actualizacion")

admin.site.register(EmpresaDatos,EmpresaAdmin)