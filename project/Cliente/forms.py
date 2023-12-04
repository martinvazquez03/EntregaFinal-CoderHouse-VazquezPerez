from django import forms
from . import models

class Usuario_form(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = "__all__"