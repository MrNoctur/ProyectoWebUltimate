from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True,default='default_usermane')
    password = models.CharField(max_length=100, default=make_password('default_password'))
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)
    # Opcional: agregar campos adicionales como teléfono, dirección, etc.

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

    #lo relacionado con el carrito
        
class Producto(models.Model):
        nombre = models.CharField(max_length=255)
        descripcion = models.TextField()
        precio = models.DecimalField(max_digits=10, decimal_places=2)
        imagen = models.URLField(blank=True)

        def __str__(self):
            return self.nombre    
    
class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField('Producto', blank=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

