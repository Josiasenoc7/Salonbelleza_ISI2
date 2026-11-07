from django.db import models

class Parametro(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    valor = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    