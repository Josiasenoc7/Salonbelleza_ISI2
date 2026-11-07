from django import forms
from .models import Cita, Cita_Empleado, Clientes_Citas, Cliente_Cita_Detalle

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['servicio', 'fecha', 'estado', 'observaciones']

class CitaEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Cita_Empleado
        fields = ['cita', 'empleado']

class ClientesCitasForm(forms.ModelForm):
    class Meta:
        model = Clientes_Citas
        fields = ['cliente', 'cita']

class ClienteCitaDetalleForm(forms.ModelForm):
    class Meta:
        model = Cliente_Cita_Detalle
        fields = ['cliente_cita', 'parametro', 'valor']