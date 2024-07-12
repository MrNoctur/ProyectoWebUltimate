from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistroForm, LoginForm
from .models import Carrito, Producto

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)

        if form.is_valid():
            nuevo_usuario = form.save()
            # Autentificar al usuario recién registrado
            login(request, nuevo_usuario)
            return redirect('index')

    form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

# Vista para el perfil de usuario (ejemplo)
def perfil(request):
    usuario = request.user
    # Mostrar información del usuario o permitir la edición del perfil
    return render(request, 'tiendaweb/perfil.html', {'usuario': usuario})

def index(request):
    context={}
    return render(request, 'index.html', context)



#te dejo comentado el avance


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

#relacionado al carrito

def ver_carrito(request):
    carrito_usuario = Carrito.objects.get(usuario=request.user)
    productos_en_carrito = carrito_usuario.productos.all()
    
    context = {
        'productos_en_carrito': productos_en_carrito
    }
    return render(request, 'carrito.html', context)


def lista_productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'productos.html', context)

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    # Verificar si el producto está en el carrito del usuario
    if request.user.carrito.filter(id=producto.id).exists():
        request.user.carrito.remove(producto)
        messages.success(request, f'El producto "{producto.nombre}" ha sido eliminado del carrito.')
    else:
        messages.error(request, 'El producto no está en tu carrito.')

    return redirect('carrito')

def finalizar_compra(request):
    # Lógica para finalizar la compra (ejemplo: limpiar el carrito, procesar pago, etc.)
    # Aquí puedes agregar la lógica necesaria para finalizar la compra según tu aplicación

    # Ejemplo: Limpiar el carrito (borrar todos los productos del carrito)
    request.user.carrito.clear()

    # Mostrar mensaje de éxito
    messages.success(request, '¡Gracias por tu compra! Tu pedido ha sido procesado correctamente.')

    # Redirigir a una página de confirmación o a la página principal
    return redirect('index')