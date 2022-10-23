from django.db import models
from django.contrib.auth.models import User
# Create your models here.

## Arreglo de opciones para concursos
opciones_estado = [
    ['ACTIVO', 'ACTIVO'],
    ['INACTIVO', 'INACTIVO']
]

## Arreglo de opciones para recetas
opciones_concurso = [
    ['Desayunos', 'Desayunos'],
    ['Almuerzos', 'Almuerzos'],
    ['Cenas', 'Cenas'],
    ['Snacks', 'Snacks']
]

class Concurso(models.Model):
    titulo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=15)
    contenido = models.TextField()
    fecha_inicio = models.DateTimeField(auto_now=True)
    fecha_termino = models.DateTimeField(auto_created=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.IntegerField(choices=opciones_estado)

    def __str__(self):
        return self.categoria[1]


class Receta(models.Model):
    titulo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=15)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
