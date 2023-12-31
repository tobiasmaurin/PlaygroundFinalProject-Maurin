from django.db import models

# Create your models here.

#Aqui estoy creando la clase anillos

class anillo (models.Model):
    tipo = models.CharField (max_length=20)          #alianza, compromizo, iniciales, otros
    material = models.CharField (max_length=20)      #oro, plata, bronce
    medida = models.IntegerField ()                  
    precio = models.IntegerField ()
    imagen = models.ImageField(upload_to='media/imagenes_anillos', null=True, blank = True)

