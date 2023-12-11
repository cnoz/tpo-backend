from django.shortcuts import render
from .models import UsuarioDato
# Create your views here.
def home(request):
    return render(request,"usuario/index.html")

def contacto(request):
    return render(request,"usuario/contacto.html")

def postularse(request):
    usuarios = UsuarioDato.objects.all()
    return render(request, "usuario/postulantes.html", {"usuarios":usuarios})


# def empresas(request):
#     return render(request, "usuario/empresas.html")

def somos( request):
    return render(request, "usuario/somos.html")