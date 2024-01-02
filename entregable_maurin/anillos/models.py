from django.db import models
from django.utils import timezone

# Create your models here.

#Aqui estoy creando la clase anillos

class anillo (models.Model):
    tipo = models.CharField (max_length=20)          #alianza, compromizo, iniciales, otros
    material = models.CharField (max_length=20)      #oro, plata, bronce
    medida = models.IntegerField ()                  
    precio = models.IntegerField ()
    fecha_de_venta = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='media/imagenes_anillos', null=True, blank = True)

