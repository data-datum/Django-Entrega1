from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField("Nombre", max_length=30)
    edad = models.PositiveIntegerField("Edad (años)")
    fecha = models.DateTimeField("Fecha de nacimiento")