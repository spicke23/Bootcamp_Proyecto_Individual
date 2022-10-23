from django.db import models

# Create your models here.
class Snippet(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name

#class SnippetForm(forms.Modelform):

opciones_contacto = [
    [0, 'Consulta'],
    [1, 'Reclamo'],
    [2, 'Felicitaciones'],
    [3, 'Sugerencias']
]
class Contact(models.Model):
    usuario = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    categoria = models.IntegerField(choices=opciones_contacto)
    mensaje = models.TextField()

    def __str__(self):
        #return self.email
        return self.usuario