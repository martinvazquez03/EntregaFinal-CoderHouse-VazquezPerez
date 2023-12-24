from django.shortcuts import render
from Cliente import models
from django.contrib.auth.decorators import login_required

# Create your views here.

def view_mainmenu(request):
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url=None
    
    return render(request, "MainM/index.html", context={"avatar_url": avatar_url})

def view_about(request):
    if request.user.is_authenticated:
        usuario = request.user
        avatar = models.Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url=None
    return render(request, "MainM/about.html", context={"avatar_url": avatar_url })