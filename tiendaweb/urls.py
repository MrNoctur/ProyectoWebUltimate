from django.urls import path
from .views import registro, perfil, index, lista_productos
from . import views
  # Importar las vistas

urlpatterns = [
    path('', index, name='index'),  # Ruta para la vista index
    path('registro/', registro, name='registro'),  # Ruta para la vista de registro
    path('perfil/', perfil, name='perfil'),  # Ruta para la vista de perfil
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('carrito/', views.ver_carrito, name='carrito'),
    path('carrito/finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/', lista_productos, name='productos'),
    path('productos/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),  # Agregar producto al carrito
    path('carrito/aumentar/<int:producto_id>/', views.aumentar_cantidad, name='aumentar_cantidad'),  # Aumentar cantidad de un producto en el carrito
    path('carrito/disminuir/<int:producto_id>/', views.disminuir_cantidad, name='disminuir_cantidad'),  # Disminuir cantidad de un producto en el carrito
    
]
