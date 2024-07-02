from django.shortcuts import render, redirect
from .forms import ClienteForm

def home(request):
    context={}
    return render(request, 'tiendaweb/index.html', context)


def registro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form  = ClienteForm()
    return render(request, 'clientes/registro_cliente.html',{'form': form})    