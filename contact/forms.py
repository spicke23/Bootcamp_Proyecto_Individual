from django import forms
from django.db.models import fields
from .models import Snippet, Contact

#class ContactForm(forms.Form):
#    nombre = forms.CharField()
#    email = forms.EmailField(label='Correo')
#    categoria = forms.ChoiceField(choices=[('0','---'),('1','Consulta'),('2','Reclamo'),('3','Felicitaciones')])
#    body = forms.CharField(label='Contenido',widget=forms.Textarea)
#    categoria.widget.attrs.update({'class': 'form-select'})

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['usuario','email','categoria','mensaje']
        #fields = '__all__'

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = {'name', 'body'}