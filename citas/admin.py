from django.contrib import admin
from .models import *

admin.site.register(Cita)
admin.site.register(Cita_Empleado)
admin.site.register(Clientes_Citas)
admin.site.register(Cliente_Cita_Detalle)