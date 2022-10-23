from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email','password1','password2']

class LoginForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput)
    clave = forms.CharField(widget=forms.PasswordInput)