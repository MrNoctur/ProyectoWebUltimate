from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo_electronico', 'contrasena']

    # Opcional: agregar validadores personalizados para los campos del formulario
