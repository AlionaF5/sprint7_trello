from django.db import models

# Create your models here.
class Tablero(models.Model):
    nombre_tablero = models.CharField(max_length=50,verbose_name='')

    def __str__(self):
        return self.nombre_tablero    

class Lista(models.Model):
    nombre_lista = models.CharField(max_length=50)
    fk_tablero = models.ForeignKey(Tablero, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre_lista

class Tarea(models.Model):
    nombre_tarea = models.CharField(max_length=50)
    descripcion = models.CharField(max_length = 255)
    fk_lista = models.ForeignKey(Lista, on_delete = models.CASCADE)

