from django.contrib import admin
from .models import Contacto
# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display=("nombre","email","asunto",)
    search_fields=("nombre",)
    readonly_fields= ("creacion",)
admin.site.register(Contacto, ContactoAdmin)