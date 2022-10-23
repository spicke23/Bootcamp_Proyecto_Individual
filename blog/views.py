from django.shortcuts import render
from .models import Post
# Create your views here.

## Metodo que redirecciona al home/index de la pagina
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html',{'posts': posts})

## Metodo que redirecciona a about de la pagina
def about(request):
    return render(request,'blog/about.html')

## Metodo que redirecciona al login de la pagina
def concursos(request):
    return render(request, 'blog/concursos.html')

## Metodo que redirecciona al login de la pagina
#def contacto(request):
#    return render(request, 'blog/contact.html')
