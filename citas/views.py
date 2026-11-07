# citas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita, Cita_Empleado, Clientes_Citas, Cliente_Cita_Detalle
from .forms import CitaForm, CitaEmpleadoForm, ClientesCitasForm, ClienteCitaDetalleForm



from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Cita

def calendario(request):
    # Solo muestra la página
    return render(request, "citas/calendario.html")

def eventos_citas(request):
    # Devuelve las citas en formato que entiende FullCalendar
    citas = Cita.objects.select_related("servicio").all()

    eventos = []
    for c in citas:
        titulo = f"{c.servicio.nombre} - {c.estado}"
        eventos.append({
            "id": c.id,
            "title": titulo,
            "start": c.fecha.isoformat(),
            # Si luego manejas duración, aquí podrías agregar "end"
        })

    return JsonResponse(eventos, safe=False)

def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, 'citas/lista_citas.html', {'citas': citas})

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm()
    return render(request, 'citas/crear_cita.html', {'form': form})

def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'citas/editar_cita.html', {'form': form})

def eliminar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('lista_citas')
    return render(request, 'citas/eliminar_cita.html', {'cita': cita})


# =========================
# VISTAS CITA_EMPLEADO
# =========================
def lista_cita_empleado(request):
    registros = Cita_Empleado.objects.all()
    return render(request, 'citas/lista_cita_empleado.html', {'registros': registros})

def crear_cita_empleado(request):
    if request.method == 'POST':
        form = CitaEmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cita_empleado')
    else:
        form = CitaEmpleadoForm()
    return render(request, 'citas/crear_cita_empleado.html', {'form': form})

def editar_cita_empleado(request, pk):
    registro = get_object_or_404(Cita_Empleado, pk=pk)
    if request.method == 'POST':
        form = CitaEmpleadoForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('lista_cita_empleado')
    else:
        form = CitaEmpleadoForm(instance=registro)
    return render(request, 'citas/editar_cita_empleado.html', {'form': form})

def eliminar_cita_empleado(request, pk):
    registro = get_object_or_404(Cita_Empleado, pk=pk)
    if request.method == 'POST':
        registro.delete()
        return redirect('lista_cita_empleado')
    return render(request, 'citas/eliminar_cita_empleado.html', {'registro': registro})


# =========================
# VISTAS CLIENTES_CITAS
# =========================
def lista_clientes_citas(request):
    registros = Clientes_Citas.objects.all()
    return render(request, 'citas/lista_clientes_citas.html', {'registros': registros})

def crear_clientes_citas(request):
    if request.method == 'POST':
        form = ClientesCitasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes_citas')
    else:
        form = ClientesCitasForm()
    return render(request, 'citas/crear_clientes_citas.html', {'form': form})

def editar_clientes_citas(request, pk):
    registro = get_object_or_404(Clientes_Citas, pk=pk)
    if request.method == 'POST':
        form = ClientesCitasForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes_citas')
    else:
        form = ClientesCitasForm(instance=registro)
    return render(request, 'citas/editar_clientes_citas.html', {'form': form})

def eliminar_clientes_citas(request, pk):
    registro = get_object_or_404(Clientes_Citas, pk=pk)
    if request.method == 'POST':
        registro.delete()
        return redirect('lista_clientes_citas')
    return render(request, 'citas/eliminar_clientes_citas.html', {'registro': registro})


# =========================
# VISTAS CLIENTE_CITA_DETALLE
# =========================
def lista_cliente_cita_detalle(request):
    registros = Cliente_Cita_Detalle.objects.all()
    return render(request, 'citas/lista_cliente_cita_detalle.html', {'registros': registros})

def crear_cliente_cita_detalle(request):
    if request.method == 'POST':
        form = ClienteCitaDetalleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cliente_cita_detalle')
    else:
        form = ClienteCitaDetalleForm()
    return render(request, 'citas/crear_cliente_cita_detalle.html', {'form': form})

def editar_cliente_cita_detalle(request, pk):
    registro = get_object_or_404(Cliente_Cita_Detalle, pk=pk)
    if request.method == 'POST':
        form = ClienteCitaDetalleForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('lista_cliente_cita_detalle')
    else:
        form = ClienteCitaDetalleForm(instance=registro)
    return render(request, 'citas/editar_cliente_cita_detalle.html', {'form': form})

def eliminar_cliente_cita_detalle(request, pk):
    registro = get_object_or_404(Cliente_Cita_Detalle, pk=pk)
    if request.method == 'POST':
        registro.delete()
        return redirect('lista_cliente_cita_detalle')
    return render(request, 'citas/eliminar_cliente_cita_detalle.html', {'registro': registro})

