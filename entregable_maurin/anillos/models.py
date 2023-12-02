from django.db import models

# Create your models here.

#Aqui estoy creando la clase anillos

class anillo (models.Model):
    tipo = models.CharField (max_length=20)
    material = models.CharField (max_length=20)
    medida = models.IntegerField ()
    precio = models.IntegerField ()
    
