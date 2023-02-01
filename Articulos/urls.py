from django.urls import path
from . import views
from .views import create_marca, delete_marca, edicionMarca, editarMarca, homeProducto, create_produc

urlpatterns = [
    path('', views.home),
    path('registrarMarca/', create_marca, name='Crear_marca'),
    path('eliminarMarca/<int:marca_id>/', delete_marca, name='borrar_marca'),
    path('edicionMarca/<int:marca_id>/', edicionMarca, name='edicion_marca'),
    path('editarMarca/<int:marca_id>/', editarMarca, name='editar_marca'),
    path('registrarProduc/', homeProducto, name='Crear_produc'),
    path('registrarProductos/', create_produc, name='Crear_productos'),

]

