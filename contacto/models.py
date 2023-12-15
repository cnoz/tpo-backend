from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre= models.CharField(max_length=30, verbose_name="Nombre")
    email= models.EmailField()
    telefono= models.IntegerField(default=000000000000, verbose_name="telefono")
    asunto= models.CharField(max_length=40, verbose_name="Asunto")
    mensaje= models.TextField()
    creacion= models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    
    def __str__(self) -> str:
        return f'{self.nombre} -- {self.asunto}'
    
    class Meta:
        verbose_name= "Motivo de contacto"
        verbose_name_plural= "Motivos de contacto"
        ordering= ["-creacion"]