from django.db import models

# Create your models here.

class UsuarioDato(models.Model):
    nombre=models.CharField(max_length=100, verbose_name="Nombre")
    apellido= models.CharField(max_length=100, verbose_name="Apellido")
    email= models.EmailField(default="none", max_length=30, verbose_name="correo electronico.")
    acercaDeMi= models.TextField()
    capacitaciones= models.TextField()
    image= models.ImageField(upload_to="datosusuarios",verbose_name="Imagen")
    link= models.URLField(verbose_name="enlace", null =True, blank = True)
    creacion= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacio")
    actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    class Meta:
        verbose_name= "Datos de Usuario"
        verbose_name_plural = "Datos de usuarios"
        ordering = ["-creacion"]