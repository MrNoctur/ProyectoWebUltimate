from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),  # Página de inicio
    path('registro/', views.registro_cliente, name='registro_cliente'),  # Página de registro
    #path('texto/', views.texto, name='texto'), #en proceso
]
