from django.urls import path
from . import views



app_name = "Cliente"

urlpatterns = [
    path("", views.view_Cliente, name = "Cliente"),
    path("usuario_buscado/", views.view_usuario_buscado, name="usuario_buscado"),
    path("crear_usuarios/", views.Formulario_usuarios, name="crear_usuarios"),
    path("mostrar_usuario_filtrado/", views.view_usuario_buscado, name="filtro_usuario"),
    path("login/", views.view_login, name="login"),
    path("logout/", views.view_logout, name="logout"),
    path("avatar/", views.crear_avatar_view, name="avatar"),
    path("editar_usuario/", views.editar_perfil_view, name="editarusuario"),
    path("eliminar_comentario/<id>", views.eliminar_comentario,name="borrarcomentario"),
    path("editar_comentario/<pk>", views.ComentarioUpdateView.as_view(), name="editarcomentario"),
    path("eleccion_comentario/<id>", views.editar_comentario, name="eleccioncomentario"),
]

