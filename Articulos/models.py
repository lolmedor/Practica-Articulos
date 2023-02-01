from django.db import models


# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=200)
    orden = models.IntegerField(default=0)


class Producto(models.Model):
    # Marca = models.ForeignKey(Marca, on_delete=models.CASCADE, blank=True, null=True, verbose_name=u'Marca'
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.FloatField(default=0)  # DecimalField
    cantidad = models.IntegerField(default=0)
    total = models.FloatField(default=0)  # DecimalField
    estado = models.BooleanField(default=True)

    @property
    def total_valores(self):
        return (self.precio * self.cantidad)

    def save(self):
        self.total = self.total_valores
        super(Producto, self).save()
