from django.shortcuts import render, redirect, get_object_or_404
from .models import Parametro
from .forms import ParametroForm

def lista_parametros(request):
    parametros = Parametro.objects.all()
    return render(request, 'parametros/lista_parametros.html', {'parametros': parametros})

def crear_parametro(request):
    if request.method == 'POST':
        form = ParametroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_parametros')
    else:
        form = ParametroForm()
    return render(request, 'parametros/crear_parametro.html', {'form': form})

def editar_parametro(request, pk):
    parametro = get_object_or_404(Parametro, pk=pk)
    if request.method == 'POST':
        form = ParametroForm(request.POST, instance=parametro)
        if form.is_valid():
            form.save()
            return redirect('lista_parametros')
    else:
        form = ParametroForm(instance=parametro)
    return render(request, 'parametros/editar_parametro.html', {'form': form})

def eliminar_parametro(request, pk):
    parametro = get_object_or_404(Parametro, pk=pk)
    if request.method == 'POST':
        parametro.delete()
        return redirect('lista_parametros')
    return render(request, 'parametros/eliminar_parametro.html', {'parametro': parametro})