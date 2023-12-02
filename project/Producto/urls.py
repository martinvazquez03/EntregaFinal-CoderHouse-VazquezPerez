from django.urls import path
from . import views

app_name = "Producto"

urlpatterns = [
    path("", views.view_Producto, name = "Producto"),
]
