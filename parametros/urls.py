from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_parametros, name='lista_parametros'),
    path('crear/', views.crear_parametro, name='crear_parametro'),
    path('editar/<int:pk>/', views.editar_parametro, name='editar_parametro'),
    path('eliminar/<int:pk>/', views.eliminar_parametro, name='eliminar_parametro'),
]