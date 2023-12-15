from django import forms
from .models import UsuarioDato

# class FormUsuario(forms.Form):
#     nombre= forms.CharField(max_length=100)
#     apellido= forms.CharField(max_length=100)
#     email= forms.EmailField()
#     acercaDeMi= forms.Textarea()
#     capacitaciones= forms.Textarea()
#     image=forms.ImageField()
#     link= forms.URLField()
    

class FormUsuario(forms.ModelForm):
    class Meta:
        model = UsuarioDato
        fields= "__all__"