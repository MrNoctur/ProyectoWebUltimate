from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)

        if form.is_valid():
            nuevo_usuario = form.save()
            # Autentificar al usuario recién registrado
            login(request, nuevo_usuario)
            return redirect('index')

    form = RegistroForm()
    return render(request, 'tiendaweb/registro.html', {'form': form})

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
