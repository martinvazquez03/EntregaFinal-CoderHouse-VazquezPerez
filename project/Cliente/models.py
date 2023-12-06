from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    usuario = models.CharField(max_length=20, null=False)
    contraseña = models.CharField(max_length=20, null=False)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    pais_origen = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    



