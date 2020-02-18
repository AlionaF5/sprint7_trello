from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('crearTablero/', views.crearTablero, name='crearTablero'),
    path('crearLista/', views.crearLista, name='crearLista'),
    path('crearTarea/', views.crearTarea, name='crearTarea'),
    path('consultarTablero/', views.consultarTablero, name='consultarTablero'),
    path('consultarLista/<int:id>', views.consultarLista, name='consultarLista'),
    path('consultarTarea/<int:id>', views.consultarTarea, name='consultarTarea'),
    path('modificarTablero/<int:id>', views.modificarTablero, name='modificarTablero'),
    path('modificarLista/<int:id>', views.modificarLista, name='modificarLista'),
    path('modificarTarea/<int:id>', views.modificarTarea, name='modificarTarea'),
    path('eliminarTablero/<int:id>', views.eliminarTablero, name='eliminarTablero'),
    path('eliminarLista/<int:id>', views.eliminarLista, name='eliminarLista'),
    path('eliminarTarea/<int:id>', views.eliminarTarea, name='eliminarTarea'),

]