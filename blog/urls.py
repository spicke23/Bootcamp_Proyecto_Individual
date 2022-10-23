from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('listar_receta/',views.concursos,name='listar_receta'),
    path('login/',include('users.urls')),
#    path('logout/', include('users.urls')),
]