from django.db import models
import datetime


# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField(verbose_name="mail del cliente")
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.apellido

class Producto(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
