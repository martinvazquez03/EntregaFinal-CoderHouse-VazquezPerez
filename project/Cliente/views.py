from django.shortcuts import render, redirect

from . import models
from datetime import date
# Create your views here.

def view_Cliente(request):
    usuario = models.Usuario.objects.all()
    context = {"Usuarios" : usuario}
    return render(request, "Cliente/index.html", context)

def crear_usuarios(request):
    p1 = models.Pais(nombre = "Perú")
    p2 = models.Pais(nombre = "Mexico")
    p3 = models.Pais(nombre = "Brasil")
    p1.save()
    p2.save()
    p3.save()
    c1 = models.Usuario(nombre = "Ignacio", apellido = "Olazabal", usuario = "Nachito750", contraseña = "123" ,fecha_nacimiento = date(2003,9,27), pais_origen = p1)
    c2 = models.Usuario(nombre = "Lautaro Esteban", apellido = "Ruggeri", usuario = "LautiRugge", contraseña = "456" ,fecha_nacimiento = date(2004,6,7), pais_origen = p2)
    c3 = models.Usuario(nombre = "Francisco", apellido = "Mackinlay", usuario = "CamelloMack", contraseña = "789" ,fecha_nacimiento = date(2003,10,22), pais_origen = p3)
    c4 = models.Usuario(nombre = "Gaspar Benjamin", apellido = "Black", usuario = "Blacky123", contraseña = "12345" ,fecha_nacimiento = date(2004,4,7), pais_origen = None)
    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("Cliente:Cliente")

def filtrar(request):
    usuario_nombre = models.Usuario.objects.filter(nombre__contains = "J")
    
    usuario_nacimiento = models.Usuario.objects.filter(fecha_nacimiento__gt = date(2004,1,1))
    
    usuario_pais_origen = models.Usuario.objects.filter(pais_origen = None)
    
    context = {"Usuario_nombre":usuario_nombre,
               "Usuario_nacimiento": usuario_nacimiento,
               "Usuario_pais_origen": usuario_pais_origen}
    return render(request, "Cliente/filtrar.html", context)

from . import forms

def Formulario_usuarios(request):
    if request.method == "POST":
        form = forms.Usuario_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cliente:Cliente")
    else:
        form = forms.Usuario_form()
    return render(request, "Cliente/crear_usuario.html", {"form": form})