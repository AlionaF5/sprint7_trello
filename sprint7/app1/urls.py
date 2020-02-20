from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crearTablero/', views.crearTablero, name='crearTablero'),
    path('crearLista/', views.crearLista, name='crearLista'),
    path('crearTarea/', views.crearTarea, name='crearTarea'),
    path('consultarTablero/', views.consultarTablero, name='consultarTablero'),
    path('consultarLista/<int:id>', views.consultarLista, name='consultarLista'),
    path('consultarTarea/<int:id>', views.consultarTarea, name='consultarTarea'),
    path('editarTablero/<int:id>', views.editarTablero, name='editarTablero'),
    path('editarLista/<int:id>', views.editarLista, name='editarLista'),
    path('editarTarea/<int:id>', views.editarTarea, name='editarTarea'),
    path('eliminarTablero/<int:id>', views.eliminarTablero, name='eliminarTablero'),
    path('eliminarLista/<int:id>', views.eliminarLista, name='eliminarLista'),
    path('eliminarTarea/<int:id>', views.eliminarTarea, name='eliminarTarea'),
    path('tablerocreado/', views.tablerocreado, name='tablerocreado'),
    path('listacreada/', views.listacreada, name='listacreada'),
    path('tareacreada/', views.tareacreada, name='tareacreada'),
    path('salir/',views.salir, name='salir'),
]
