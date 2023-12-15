from django.shortcuts import render, redirect
from .models import UsuarioDato
from  .forms import FormUsuario

# Create your views here.
def home(request):
    return render(request,"usuario/index.html")

def contacto1(request):
    return render(request,"usuario/contacto1.html")

def postularse(request):
    usuarios = UsuarioDato.objects.all()
    return render(request, "usuario/postulantes.html", {"usuarios":usuarios})


# def empresas(request):
#     return render(request, "usuario/empresas.html")

def somos( request):
    return render(request, "usuario/somos.html")

def api_postulante(request):
    if request.method == "POST":
        formulario = FormUsuario(request.POST)
        if formulario.is_valid():
            
            informacion = formulario.cleaned_data
            datousuario= UsuarioDato(nombre = informacion['nombre'], 
                                    apellido = informacion['apellido'],
                                    email=informacion['email'],
                                    acercaDeMi = informacion['acercaDeMi'],
                                    capacitaciones=informacion['capacitaciones'],
                                    image= informacion['image'],
                                    link= informacion['link'])
            datousuario.save()
            return redirect('postularse')
    else:
        formulario= FormUsuario()
    return render (request, "usuario/api_postulante.html",{'formulario':formulario})
    
    
    
