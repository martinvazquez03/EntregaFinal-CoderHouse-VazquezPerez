from django.shortcuts import render, redirect
from . import forms, models
from Cliente import models
from django.contrib.auth.decorators import login_required
from Cliente import forms
# Create your views here.

def view_Producto(request):
    todos_los_videos = models.Videos.objects.all()
    todos_los_comentarios = models.Comentario.objects.all()
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
        
    else:
        avatar_url=None
    
    return render(request, "Producto/index.html", context= {"avatar_url":avatar_url,"videos": todos_los_videos,"comentarios":todos_los_comentarios})




def comentar_view(request):
    
    usuario = request.user

    if request.method == "GET":
        formulario = forms.Comentarform()
        return render(request,"Producto/comentarios.html",context={"form": formulario, "usuario": usuario})
    else:
        formulario = forms.Comentarform(data=request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = models.Comentario(autor=usuario, post=informacion["post"], texto=informacion["texto"])
            modelo.save()
            return redirect("Producto:Producto")

    
