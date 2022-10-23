from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.listar_comentarios,name='contact'),
    #path('',views.listar_comentarios,name='listar_comentarios'),
    path('fomulario',views.formulario,name='formulario'),
    path('snippet/',views.snippet_detail,name='snippet'),
]