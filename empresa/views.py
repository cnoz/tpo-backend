from django.shortcuts import render
from .models import EmpresaDatos

# Create your views here.
def empresas(request):
    datosempresas=EmpresaDatos.objects.all()
    return render(request, "empresa/empresas.html",{"datosempresas":datosempresas} )

