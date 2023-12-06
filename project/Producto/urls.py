from django.urls import path
from . import views

app_name = "Producto"

urlpatterns = [
    path("", views.view_Producto, name = "Producto"),
    path("comentar/", views.view_comentar, name="comentar"),
    path("comentarios/", views.view_comentarios, name = "comentarios")
]
