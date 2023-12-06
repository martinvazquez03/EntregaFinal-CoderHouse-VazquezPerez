from django.shortcuts import render, redirect

from . import models
from datetime import date
# Create your views here.

def view_Cliente(request):
    usuario = models.Usuario.objects.all()
    context = {"Usuarios" : usuario}
    return render(request, "Cliente/index.html", context)


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