from django.contrib import admin
from .models import UsuarioDato
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields= ("creacion","actualizacion")
    list_display=("nombre","apellido","email")
    list_filter=("creacion",)    
    date_hierarchy="creacion"
    
admin.site.register(UsuarioDato,UsuarioAdmin)