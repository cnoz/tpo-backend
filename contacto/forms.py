from django import forms
from .models import Contacto
# from .models import Contacto

# class FormContacto(forms.Form):
#     nombre= forms.CharField(max_length=30)
#     email= forms.EmailField()
#     telefono= forms.IntegerField()
#     asunto= forms.CharField(max_length=40)
#     mensaje= forms.Textarea()
    

class FormContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields= "__all__"