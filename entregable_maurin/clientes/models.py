from django.db import models

# Create your models here.

# aca se crea la clase cliente

class cliente (models.model):
    nombre = models.CharField (max_length=50)
    dni = models.IntegerField ()
    email = models.EmailField ()
    celular = models.IntegerField ()
    