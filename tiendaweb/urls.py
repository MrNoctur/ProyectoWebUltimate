from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('registro/', views.registro_cliente, name='registro_cliente'),  # Página de registro
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:pk>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),



]

