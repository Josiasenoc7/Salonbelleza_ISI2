from django.db import models
from .validators import validar_telefono_hn

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefono = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        validators=[validar_telefono_hn]
    )
    rol = models.ForeignKey(Rol, on_delete=models.RESTRICT)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre