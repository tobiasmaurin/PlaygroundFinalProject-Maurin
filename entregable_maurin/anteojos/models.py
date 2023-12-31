from django.db import models
from django.utils import timezone
# Create your models here.

# aqui se crea la clase de anteojos


class anteojo (models.Model):
    tipo = models.CharField (max_length=50)           # de sol o de ver
    marca = models.CharField (max_length=30)          # zero, rayban, etc
    color = models.CharField (max_length=20)          # negro, marron, etc
    tamanio = models.CharField (max_length=20)        # chico, mediano, grande
    fecha_de_venta = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='media/imagenes_anteojos', null=True, blank = True)

