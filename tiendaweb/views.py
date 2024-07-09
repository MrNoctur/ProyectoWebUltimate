from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, AgregarAlCarritoForm, ActualizarCantidadForm
from .models import Cliente, Producto, Carrito, ItemCarrito

def home(request):
    context={}
    return render(request, 'index.html', context)


def registro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
        
    else:
        form  = ClienteForm()
    return render(request, 'registro_cliente.html',{'form': form}) 

#te dejo comentado el avance

# Vista para listar todos los clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

# Vista para ver los detalles de un cliente específico
def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/detalle_cliente.html', {'cliente': cliente})

# Vista para editar un cliente existente
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes/lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'registro_cliente.html', {'form': form})

# Vista para eliminar un cliente
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})


#productos

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tiendaweb/listar_productos.html', {'productos': productos})



