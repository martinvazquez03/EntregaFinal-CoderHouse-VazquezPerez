from django.shortcuts import render, redirect

from . import models
from . import forms
# Create your views here.

def view_Cliente(request):
    usuario = models.Usuario.objects.all()
    context = {"Usuarios" : usuario}
    return render(request, "Cliente/index.html", context)


def Formulario_usuarios(request):
    if request.method == "POST":
        form = forms.Usuario_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cliente:Cliente")
    else:
        form = forms.Usuario_form()
    return render(request, "Cliente/crear_usuario.html", {"form": form})


def view_usuario_buscado(request):
    if request.method == "GET":
        form_filtro = forms.Buscar_Usuario_Form()
        context = {"Form" : form_filtro}
        return render(request, "Cliente/buscar_usuario.html", context)
    else:
        format = forms.Buscar_Usuario_Form(request.POST)
        if format.is_valid():
            info = format.cleaned_data
            filtro_usuarios = []
            for usuario in models.Usuario.objects.filter(usuario=info["usuario"]):
                filtro_usuarios.append(usuario)
            contexto_filtro = {"Filtro": filtro_usuarios}
            return render(request, "Cliente/mostrar_filtro_usuario.html", contexto_filtro)
    
    

    