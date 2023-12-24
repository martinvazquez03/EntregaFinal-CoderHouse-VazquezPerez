from django.db import models
from django.contrib.auth.models import User

 

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(default="avatares/avatar_predeterminado.webp", upload_to='avatares/', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"


class Videos(models.Model):
    video = models.FileField(upload_to="videos/", null=True, blank=True)
    titulo = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.titulo}"


class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.CharField(max_length=2200)
    post = models.ForeignKey(Videos, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.autor}: '{self.post}'"
