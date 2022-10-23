from django.urls import path, include
from . import views

urlpatterns = [
    #path('concurso/',views.muestra_concursos,name='concurso'),
    #path('concurso/',views.inscipcion_concurso,name='concurso'),
    #path('agregar_concurso/',views.agregar_concurso,name='agregar_concurso'),
    path('',views.listar_receta,name='listar_receta'),
    path('agregar_receta/',views.agregar_receta,name='agregar_receta'),
    path('editar_receta/<int:id>/',views.editar_receta,name='editar_receta'),
    path('eliminar_receta/<int:id>/',views.eliminar_receta,name='eliminar_receta'),
]