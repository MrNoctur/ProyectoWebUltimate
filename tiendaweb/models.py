from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)

    # Opcional: agregar campos adicionales como teléfono, dirección, etc.

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
        
        