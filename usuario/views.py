from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "usuario/index.html")


def postularse(request):
    pass



def empresas(request):
    pass

def contacto(request):
    pass