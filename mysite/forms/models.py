from django.db import models

# Create your models here.
from django.db import models


class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    fecha_de_nacimiento = models.DateField()
    email = models.EmailField(max_length=254)
    direccion = models.CharField(max_length=250)
