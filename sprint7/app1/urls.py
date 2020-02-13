from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('crearTablero/', views.crearTablero, name='crearTablero'),
    path('crearLista/', views.crearLista, name='crearLista'),
    path('crearTarea/', views.crearTarea, name='crearTarea'),
]