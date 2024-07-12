from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)

    # Opcional: agregar campos adicionales como teléfono, dirección, etc.

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
        
        