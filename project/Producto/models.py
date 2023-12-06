from django.db import models
from Cliente.models import Usuario
# Create your models here.

class Comentarios(models.Model):
    autor = models.CharField(max_length=20, help_text="(ingrese su nombre de usuario)")
    comentario = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.autor}\n {self.comentario}"