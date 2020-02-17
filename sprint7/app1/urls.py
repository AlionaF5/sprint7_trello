from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crearTablero/', views.crearTablero, name='crearTablero'),
    path('crearLista/', views.crearLista, name='crearLista'),
    path('crearTarea/', views.crearTarea, name='crearTarea'),
    path('consultarTablero/', views.consultarTablero, name='consultarTablero'),
    path('consultarLista/', views.consultarLista, name='consultarLista'),
    path('consultarTarea/', views.consultarTarea, name='consultarTarea'),
]
