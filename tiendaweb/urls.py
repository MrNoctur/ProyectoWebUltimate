from django.urls import path
from .views import registro, perfil, index
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
]
