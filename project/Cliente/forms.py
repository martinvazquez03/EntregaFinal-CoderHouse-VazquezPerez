from django import forms
from . import models

class Usuario_form(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = "__all__"
        
        
class Buscar_Usuario_Form(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ["usuario"]