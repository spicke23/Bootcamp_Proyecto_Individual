from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.salir,name='logout'),
    path('listar_usuarios/',views.listar_usuarios,name='listar_usuarios'),
    path('editar_datos_personales/<int:id>/',views.editar_datos_personales,name='editar_datos_personales'),
    path('listar_post/<int:id>/',views.listar_post,name='listar_post'),
    path('listar_recetas/<int:id>/',views.listar_recetas,name='listar_recetas'),
]