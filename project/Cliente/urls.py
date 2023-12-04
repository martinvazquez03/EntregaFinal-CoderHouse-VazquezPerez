from django.urls import path
from . import views

app_name = "Cliente"

urlpatterns = [
    path("", views.view_Cliente, name = "Cliente"),
    path("Crear_Usuarios/", views.crear_usuarios, name = "Crear_Usuarios"),
    path("Usuarios_filtrados/", views.filtrar, name = "Usuarios_filtrados"),
    path("crear_usuarios/", views.Formulario_usuarios, name = "crear_usuarios")
]
