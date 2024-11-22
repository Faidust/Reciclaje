
from django.db import models
from django.contrib.auth.models import User

class Palabra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Palabra = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.usuario.username} - {self.palabra} - {self.cantidad}'

class Reciclaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.usuario.username} - {self.material} - {self.cantidad}'

# Create your models here.
