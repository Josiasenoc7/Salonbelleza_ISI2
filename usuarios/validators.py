import re
from django.core.exceptions import ValidationError

def validar_telefono_hn(value: str):
    """
    Honduras: usualmente 8 dígitos (sin espacios ni guiones).
    Ej: 98765432
    """
    if value is None or value == "":
        return  # si permites teléfono opcional

    if not re.fullmatch(r"\d{8}", value):
        raise ValidationError("El teléfono debe tener exactamente 8 dígitos (ej: 98765432).")