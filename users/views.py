from pyexpat import model
from django.shortcuts import redirect, render
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Post
from concurso.models import Receta

# Create your views here.

def register(request):
    data = {
        'form': UserRegisterForm()
    }
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            data['mensaje'] = 'Te has registrado exitosamente'
            return redirect('login')
        data['form'] = form
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',data)

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():            
            nombre = form.cleaned_data['nombre']
            clave = form.cleaned_data['clave']
            user = authenticate(request,username=nombre,password=clave)
            if user is not None:
                auth_login(request,user)
                return render(request,'users/profile.html',{'user': user})
            else:
                return redirect('/login')
    else:
        form=LoginForm()
        return render(request,'users/login.html',{'form': form})


def listar_usuarios(request):
    usuarios = {
    'users': User.objects.raw('SELECT * FROM auth_user'),
    'id': 1
    }
    return render(request,'users/listar_usuarios.html',usuarios)

@login_required(login_url='login')
def profile(request):
    return render(request,'users/profile.html')

@login_required(login_url='login')
def salir(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def editar_datos_personales(request, id):
    user = User.objects.get(pk=id)
    form = UserRegisterForm(instance=user)
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST,instance=user)
        form.save()
        #return redirect('profile')
        return render(request,'users/profile.html',{'user': user})
    else:
        return render(request,'users/editar_datos_personales.html',{'form': form})


@login_required(login_url='login')
def listar_post(request,id):
    #posts = Post.objects.all()
    posts = Post.objects.get(pk=id)
    return render(request,'users/listar_post.html',{'posts': posts})


@login_required(login_url='login')
def listar_recetas(request,id):
    #posts = Post.objects.all()
    posts = Receta.objects.raw('SELECT * FROM blog.concurso_receta WHERE autor_id = id')
    return render(request,'users/listar_recetas.html',{'posts': posts})
