from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm
from .models import Contact

# Create your views here.

def formulario(request):
    data = {
        'form': ContactForm()
    }
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            data['mensaje'] = 'Mensaje enviado correctamente'
    else:
        data['form'] = ContactForm()
    return render(request, 'contact/forms.html',data)

def listar_comentarios(request):
    comentarios = {
    'coments': Contact.objects.all(),
    'id': 1
    }
    return render(request,'contact/listar_comentarios.html',comentarios)

#def formulario(request):
#    return render(request,'contact/forms.html')









####################################
def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            print("Snippet funciona")
    form = SnippetForm()
    return render(request, 'contact/forms.html',{'form': form})