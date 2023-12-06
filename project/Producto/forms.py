from django import forms
from . import models

class Comentarios_form(forms.ModelForm):
    class Meta:
        model = models.Comentarios
        fields = "__all__"