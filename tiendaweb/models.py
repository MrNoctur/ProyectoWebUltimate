from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class generoCli(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return str(self.genero)
    
class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey('generoCli',on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.IntegerField()

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"
    


# se agrega el model del producto y del carrito    
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
    

class Carrito(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.producto.precio
        super().save(*args, **kwargs)
        self.carrito.total = sum(item.subtotal for item in self.carrito.items.all())
        self.carrito.save()