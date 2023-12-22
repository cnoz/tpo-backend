from django import forms
from .models import Contacto

class FormContacto(forms.Form):
    nombre= forms.CharField(max_length=30)
    email= forms.EmailField()
    telefono= forms.IntegerField()
    asunto= forms.CharField(max_length=40)
    mensaje= forms.CharField(max_length=100)
            
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['telefono'].initial = 54

### De esta forma tambien funciona
# class FormContacto(forms.ModelForm):
#     class Meta:
#         model = Contacto
#         fields= "__all__"