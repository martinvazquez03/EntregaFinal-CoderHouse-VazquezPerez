from django.urls import path
from . import views

app_name = "Cliente"

urlpatterns = [
    path("", views.view_Cliente, name = "Cliente"),
    path("usuario_buscado/", views.view_usuario_buscado, name = "usuario_buscado"),
    path("crear_usuarios/", views.Formulario_usuarios, name = "crear_usuarios"),
    path("mostrar_usuario_filtrado/", views.view_usuario_buscado, name = "filtro_usuario")
]
