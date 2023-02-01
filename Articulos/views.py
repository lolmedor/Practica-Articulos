from django.shortcuts import render, redirect
from .models import Marca, Producto
from django.contrib import messages


def home(request):
    Marcaslistas = Marca.objects.all()
    messages.success(request, '¡Marcas Registradas!')
    return render(request, "gestionMarcas.html", {"marcas": Marcaslistas})


def homeProducto(request):
    Produclistas = Producto.objects.all()
    Marcaslistas = Marca.objects.all()
    messages.success(request, '¡Productos Registrados!')
    return render(request, "gestionProducto.html", {"produc": Produclistas, "marcas": Marcaslistas})


def create_marca(request):
    marca = Marca(nombre=request.POST['txtNombre'], orden=request.POST['numOrden'])
    marca.save()
    messages.success(request, '¡Marca registrado!')
    return redirect('/')


def create_produc(request):
    produc = Producto( nombre=request.POST['txtNombre'],
                      precio=request.POST['precio'], cantidad=request.POST['cantidad'],
                      estado=request.POST['estado'])

    produc.save()
    messages.success(request, '¡Producto registrado!')
    return redirect('/')


def delete_marca(request, marca_id):
    marca = Marca.objects.get(id=marca_id)
    marca.delete()
    messages.success(request, '¡Marca eliminada!')
    return redirect('/')


def edicionMarca(request, marca_id):
    marca = Marca.objects.get(id=marca_id)
    return render(request, "edicionMarca.html", {"marca": marca})


def editarMarca(request, marca_id):
    codigo = marca_id
    nombre = request.POST['txtNombre']
    numOr = request.POST['numOrden']
    marca = Marca.objects.get(id=codigo)
    marca.nombre = nombre
    marca.orden = numOr
    marca.save()

    messages.success(request, '¡Marca actualizada!')

    return redirect('/')
