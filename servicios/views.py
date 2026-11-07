# servicios/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Servicio
from .forms import ServicioForm

def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/lista_servicios.html', {'servicios': servicios})

def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios')
    else:
        form = ServicioForm()
    return render(request, 'servicios/crear_servicio.html', {'form': form})

def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'servicios/editar_servicio.html', {'form': form})

def eliminar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('lista_servicios')
    return render(request, 'servicios/eliminar_servicio.html', {'servicio': servicio})