from django.db import models
from usuarios.models import Usuario
from servicios.models import Servicio
from parametros.models import Parametro
from django.core.exceptions import ValidationError
from django.utils import timezone

class Cita(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.RESTRICT)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=30, default='PENDIENTE')
    observaciones = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def clean(self):
        if self.fecha and self.fecha < timezone.now():
            raise ValidationError({"fecha": "No puedes crear una cita en una fecha/hora pasada."})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Cita {self.id} - {self.servicio.nombre}"

class Clientes_Citas(models.Model):
    cliente = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    cita = models.ForeignKey("citas.Cita", on_delete=models.CASCADE)

    def clean(self):
        if not self.cliente_id or not self.cita_id:
            return

        fecha = self.cita.fecha
        choque = Clientes_Citas.objects.filter(
            cliente_id=self.cliente_id,
            cita__fecha=fecha
        )
        if self.pk:
            choque = choque.exclude(pk=self.pk)

        if choque.exists():
            raise ValidationError("Este cliente ya tiene una cita en esa fecha y hora.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

class Cita_Empleado(models.Model):
    cita = models.ForeignKey("citas.Cita", on_delete=models.CASCADE)
    empleado = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cita - Empleado"
        verbose_name_plural = "Citas - Empleados"
        constraints = [
            # Esto evita duplicar EXACTAMENTE la misma relación
            models.UniqueConstraint(fields=["cita", "empleado"], name="uq_cita_empleado_unico"),
        ]

    def clean(self):
        """
        Evita que el mismo empleado tenga otra cita en la misma fecha/hora.
        """
        if not self.cita_id or not self.empleado_id:
            return

        fecha = self.cita.fecha

        choque = Cita_Empleado.objects.filter(
            empleado_id=self.empleado_id,
            cita__fecha=fecha
        )

        # si estás editando, excluye el mismo registro
        if self.pk:
            choque = choque.exclude(pk=self.pk)

        if choque.exists():
            raise ValidationError("Este empleado ya tiene una cita programada en esa fecha y hora.")

    def save(self, *args, **kwargs):
        self.full_clean()  # obliga a correr clean() siempre
        return super().save(*args, **kwargs)

class Cliente_Cita_Detalle(models.Model):
    cliente_cita = models.ForeignKey(Clientes_Citas, on_delete=models.CASCADE)
    parametro = models.ForeignKey(Parametro, on_delete=models.CASCADE)
    valor = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.cliente_cita} - {self.parametro.nombre}"
    

