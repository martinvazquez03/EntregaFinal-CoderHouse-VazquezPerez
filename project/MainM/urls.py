from django.urls import path
from . import views

app_name = "MainM"

urlpatterns = [
    path("", views.view_mainmenu, name = "MainM"),
]
