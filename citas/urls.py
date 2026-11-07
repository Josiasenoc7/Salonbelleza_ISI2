from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Cita
    path('', views.lista_citas, name='lista_citas'),
    path('crear/', views.crear_cita, name='crear_cita'),
    path('editar/<int:pk>/', views.editar_cita, name='editar_cita'),
    path('eliminar/<int:pk>/', views.eliminar_cita, name='eliminar_cita'),

    # Rutas para Cita_Empleado
    path('empleado/', views.lista_cita_empleado, name='lista_cita_empleado'),
    path('empleado/crear/', views.crear_cita_empleado, name='crear_cita_empleado'),
    path('empleado/editar/<int:pk>/', views.editar_cita_empleado, name='editar_cita_empleado'),
    path('empleado/eliminar/<int:pk>/', views.eliminar_cita_empleado, name='eliminar_cita_empleado'),

    # Rutas para Clientes_Citas
    path('clientes/', views.lista_clientes_citas, name='lista_clientes_citas'),
    path('clientes/crear/', views.crear_clientes_citas, name='crear_clientes_citas'),
    path('clientes/editar/<int:pk>/', views.editar_clientes_citas, name='editar_clientes_citas'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_clientes_citas, name='eliminar_clientes_citas'),

    # Rutas para Cliente_Cita_Detalle
    path('detalle/', views.lista_cliente_cita_detalle, name='lista_cliente_cita_detalle'),
    path('detalle/crear/', views.crear_cliente_cita_detalle, name='crear_cliente_cita_detalle'),
    path('detalle/editar/<int:pk>/', views.editar_cliente_cita_detalle, name='editar_cliente_cita_detalle'),
    path('detalle/eliminar/<int:pk>/', views.eliminar_cliente_cita_detalle, name='eliminar_cliente_cita_detalle'),

    path("calendario/", views.calendario, name="calendario_citas"),
    path("api/eventos/", views.eventos_citas, name="eventos_citas"),
]