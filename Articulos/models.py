from django.db import models


# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=200)
    orden = models.IntegerField(default=0)


class Producto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    cantidad = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    estado = models.BooleanField(default=True)


