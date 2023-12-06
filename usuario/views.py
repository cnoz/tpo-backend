from django.shortcuts import render

# Create your views here.
def home(request):
<<<<<<< HEAD
    return render(request,"usuario/index.html")

def contacto(request):
    return render(request,"usuario/contacto.html")

def empresas(request):
    return render(request,"usuario/empresas.html")

def postulantes(request):
    return render(request,"usuario/postulantes.html")

# def postularse(request):
#     pass



# def empresas(request):
#     pass
=======
    return render(request, "usuario/index.html")


def postularse(request):
    pass



def empresas(request):
    pass

def contacto(request):
    pass
>>>>>>> 1c8a6bbe9256083fafe17d261e44fcb9a964462b
