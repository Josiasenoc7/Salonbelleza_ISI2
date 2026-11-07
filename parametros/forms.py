from django import forms
from .models import Parametro

class ParametroForm(forms.ModelForm):
    class Meta:
        model = Parametro
        fields = ['nombre', 'valor', 'descripcion', 'activo']