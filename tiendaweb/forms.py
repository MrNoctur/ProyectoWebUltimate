from django import forms
from .models import Cliente, ItemCarrito

class ClienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = [
            'rut', 'nombre', 'apellido_paterno', 'apellido_materno',
            'fecha_nacimiento', 'id_genero', 'telefono', 'email', 'direccion', 'activo', 'password'
        ]

class AgregarAlCarritoForm(forms.ModelForm):
    class Meta:
        model = ItemCarrito
        fields = ['producto', 'cantidad']

class ActualizarCantidadForm(forms.ModelForm):
    class Meta:
        model = ItemCarrito
        fields = ['cantidad']

class EliminarItemForm(forms.ModelForm):
    class Meta:
        model = ItemCarrito
        fields = []