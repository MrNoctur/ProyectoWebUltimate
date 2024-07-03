from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('registro/', views.registro_cliente, name='registro_cliente'),  # Página de registro
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('cliente/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),
    path('cliente/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('cliente/<int:pk>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
]

