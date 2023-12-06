from django.shortcuts import render, redirect
from . import forms, models
# Create your views here.

def view_Producto(request):
    return render(request, "Producto/index.html")


def view_comentar(request):
    if request.method == "POST":
        form_comentario = forms.Comentarios_form(request.POST)
        if form_comentario.is_valid():
            form_comentario.save()
            return redirect("Producto:Producto")
    else:
        form_comentario = forms.Comentarios_form()
    return render(request, "Producto/comentarios.html", {"form_comentario": form_comentario})

def view_comentarios(request):
    autor = models.Comentarios.objects.all()
    context = {"Autor" : autor}
    return render(request, "Producto/ver_comentarios.html", context)