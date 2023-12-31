from django.db import models

# Create your models here.

    
    
class EmpresaDatos(models.Model):
    nombreEmpresa = models.CharField(max_length=100, verbose_name="Titulo")
    ubicacion= models.CharField(max_length=100, verbose_name="Ubicacion")
    descripcionEmpresa= models.TextField(max_length=200,verbose_name="Descripcion")
    puestoBuscado=models.CharField(max_length=200, verbose_name="Puesto buscado")
    requisitos= models.TextField()
    beneficios= models.TextField()
    image= models.ImageField(default="\image-empresa-defautl.png",null=True,blank=True,verbose_name="Imagen", upload_to="projectempresa")
    email= models.EmailField(default="none@tumail.com",null=True,blank=True ,max_length=30, verbose_name="Correo de contacto.")
    link= models.URLField(verbose_name="enlace", null =True, blank = True)
    creacion= models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    actualizacion= models.DateTimeField(auto_now=True,verbose_name="Fecha de modificacion")
    
    def __str__(self):
        return self.nombreEmpresa
    
    class Meta:
        verbose_name= "Empresa Dato"
        verbose_name_plural= "Empresa Datos"
        ordering= ["-creacion"]