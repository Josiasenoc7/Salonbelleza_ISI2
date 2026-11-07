from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    # Apps
    path('citas/', include('citas.urls')),          # Aquí van Cita, Cita_Empleado, Clientes_Citas, Cliente_Cita_Detalle
    path('parametros/', include('parametros.urls')),
    path('servicios/', include('servicios.urls')),
    path('usuarios/', include('usuarios.urls')),

    # Redirigir la raíz a lista de citas
    path('', lambda request: redirect('lista_citas')),
]