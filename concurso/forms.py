from django import forms
from django.db.models import fields
from .models import Concurso, Receta

class ConcursoForm(forms.ModelForm):
    class Meta:
        model = Concurso
        #fields = ['usuario','email','categoria','mensaje']
        fields = '__all__'

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        #fields = ['usuario','email','categoria','mensaje']
        fields = '__all__'