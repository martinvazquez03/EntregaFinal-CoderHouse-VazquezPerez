from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView,UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms, models


# Create your views here.

def view_Cliente(request): 
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url=None
    
    usuarios = UsuarioListView().get_queryset()
    return render(request, "Cliente/index.html", context={"Usuarios" : usuarios, "avatar_url" : avatar_url})




class UsuarioListView(ListView):
    model = UserModel
    context_object_name = "Usuarios"
    template_name = "Cliente/index.html"


def Formulario_usuarios(request):
    if request.method == "POST":
        form = forms.CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cliente:login")
    else:
        form = forms.CrearUsuarioForm()
    return render(request, "Cliente/crear_usuario.html", {"form": form})


def view_usuario_buscado(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            form_filtro = forms.BuscarUsuarioForm()
            context = {"Form": form_filtro}
            return render(request, "Cliente/buscar_usuario.html", context)
        elif request.method == "POST":
            form = forms.BuscarUsuarioForm(request.POST)
            if form.is_valid():
                info = form.cleaned_data
                filtro_usuarios = User.objects.filter(username=info['username'])
                contexto_filtro = {"Filtro": filtro_usuarios}
                return render(request, "Cliente/mostrar_filtro_usuario.html", contexto_filtro)
            else:
                context = {"Form": form}
                return render(request, "Cliente/buscar_usuario.html", context)
    else: return redirect("Cliente:login")
        

def view_login(request):
    if request.method=="GET":
        return render(request, "Cliente/login.html", {"form":AuthenticationForm()})
    else:
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            contraseña = informacion["password"]
            modelo = authenticate(username=usuario,password=contraseña)
            login(request,modelo)
            return redirect("Cliente:Cliente")
        else:
            return render(request, "Cliente/login.html", {"form":formulario})
        
        
@login_required
def view_logout(request):
    if request.method=="GET":
        logout(request)
        return redirect("Cliente:Cliente")
    



def crear_avatar_view(request):
    if request.user.is_authenticated:
        usuario = request.user

        if request.method == "GET":
            formulario = forms.UserAvatarFormulario()
            return render(request,"Cliente/avatar.html",context={"form": formulario, "usuario": usuario})
        else:
            formulario = forms.UserAvatarFormulario(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                modelo = models.Avatar(user=usuario, imagen=informacion["imagen"])
                modelo.save()
                return redirect("Cliente:Cliente")
    else: return redirect("Cliente:login")
        
        
@login_required
def editar_perfil_view(request):
    usuario = request.user
    avatar = models.Avatar.objects.filter(user=usuario).last()
    avatar_url = avatar.imagen.url if avatar is not None else ""
    if request.method == "GET":
        valores_iniciales = {"email": usuario.email, "nombre": usuario.first_name, "apellido": usuario.last_name,}
        formulario = forms.UserEditionFormulario(initial=valores_iniciales)
        return render(
            request,"Cliente/editar_usuario.html",context={"form": formulario, "usuario": usuario, "avatar_url": avatar_url})
    else:
        formulario = forms.UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.email = informacion["email"]
            usuario.set_password(informacion["password1"])
            usuario.first_name = informacion["nombre"]
            usuario.last_name = informacion["apellido"]
            usuario.save()
        return redirect("Cliente:Cliente")


def eliminar_comentario(request, id):
    instance = get_object_or_404(models.Comentario, id=id)
    if instance.autor != request.user:
        response = {"mensaje":"No tienes permiso para realizar esta accion (403)"}
        return render(request,"Cliente/accion_invalida.html" ,response)
    else:
        comentario_a_eliminar = models.Comentario.objects.filter(autor=request.user).first()
        comentario_a_eliminar.delete()
        return redirect("Producto:Producto")
    
    
    
def editar_comentario(request, id):
    instance = get_object_or_404(models.Comentario, id=id)
    if instance.autor != request.user:
        response = {"mensaje":"No tienes permiso para realizar esta accion (403)"}
        return render(request,"Cliente/accion_invalida.html" ,response)
    else:
        return redirect("Cliente:editarcomentario",id)
        
        
        
class ComentarioUpdateView(LoginRequiredMixin, UpdateView):
        model = models.Comentario
        template_name = "Cliente/editar_comentario.html"
        form_class = forms.Editarcomentarioform
        success_url = reverse_lazy("Producto:Producto")
        
