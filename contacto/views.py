from django.shortcuts import render, redirect
from .models import Contacto
from .forms import FormContacto
# Create your views here.


def contacto(request):
    if request.method == 'POST':
        formulario= FormContacto(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            datocontacto = Contacto(nombre= informacion['nombre'],
                                    email= informacion['email'],
                                    telefono= informacion['telefono'],
                                    asunto= informacion['asunto'],
                                    mensaje= informacion['mensaje']
                                   )
            datocontacto.save()
            
            return redirect ('/')
    
    else:
        formulario= FormContacto()  
    return render(request, "contacto/contacto.html", {'formulario':formulario})