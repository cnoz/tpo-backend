from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"usuario/index.html")

def contacto(request):
    return render(request,"usuario/contacto.html")

# def postularse(request):
#     pass



# def empresas(request):
#     pass
