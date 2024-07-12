from django.urls import path
from .views import registro, perfil, index  # Importar las vistas

urlpatterns = [
    path('', index, name='index'),  # Ruta para la vista index
    path('registro/', registro, name='registro'),  # Ruta para la vista de registro
    path('perfil/', perfil, name='perfil'),  # Ruta para la vista de perfil
]