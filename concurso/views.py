from django.shortcuts import render, redirect
from .models import Concurso, Receta
from .forms import ConcursoForm, RecetaForm

# Create your views here.

def agregar_concurso(request):
    form = ConcursoForm()
    if request.method == 'POST':
        form = ConcursoForm(data=request.POST)
        concurso = form.save(commit=False)
        concurso.save()
        return redirect('concurso')
    else:
        return render(request,'concurso/agregar_concurso.html',{'form': form})


## Metodo que lista los concursos activos y realizados
def muestra_concursos(request):
    context = {
        'concursos': Concurso.objects.all()
    }
    return render(request,'concurso/concurso.html',context)

def inscipcion_concurso(request):
    data = {
        'form': ConcursoForm()
    }
    if request.method == 'POST':
        form = ConcursoForm(data=request.POST)
        if form.is_valid():
            form.save()
            data['mensaje'] = 'Te has registrado exitosamente'
            return redirect('home')
        data['form'] = ConcursoForm()
    else:
        form = ConcursoForm()
    return render(request,'concurso/formulario_concurso.html',data)


## CRUD para recetas

## agregar
def agregar_receta(request):
    form = RecetaForm()
    if request.method == 'POST':
        form = RecetaForm(data=request.POST)
        receta = form.save(commit=False)
        receta.save()
        return redirect('listar_receta')
    else:
        return render(request,'concurso/agregar_receta.html',{'form': form})

## listar
def listar_receta(request):
    recetas = Receta.objects.all()
    return render(request,'concurso/receta.html',{'recetas': recetas})

## editar
def editar_receta(request,id):
    receta = Receta.objects.get(pk=id)
    form = RecetaForm(instance=receta)
    if request.method == 'POST':
        form = RecetaForm(data=request.POST,instance=receta)
        form.save()
        return redirect('listar_receta')
    else:
        return render(request,'concurso/editar_receta.html',{'form': form})

## eliminar
def eliminar_receta(request,id):
    receta = Receta.objects.get(pk=id)
    receta.delete()
    return redirect('listar_receta')
