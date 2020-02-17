from django.shortcuts import render, redirect
from django.forms import ModelForm
from app1.models import Tablero, Lista, Tarea

# Create your views here.
class TableroForm(ModelForm):
	class Meta:
		model = Tablero
		fields = ['nombre_tablero']

class ListaForm(ModelForm):
	class Meta:
		model = Lista
		fields = ['nombre_lista', 'fk_tablero']

class TareaForm(ModelForm):
	class Meta:
		model = Tarea
		fields = ['nombre_tarea', 'descripcion', 'fk_lista']

def crearTablero(request):
	form = TableroForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('app1:consultarTablero')
	return render(request, 'app1/crearTablero.html', {'form':form})

def crearLista(request):
	form = ListaForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('app1:consultarLista')
	return render(request, 'app1/crearLista.html', {'form':form})

def crearTarea(request):
	form = TareaForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('app1:consultarTarea')
	return render(request, 'app1/crearTarea.html', {'form':form})

def consultarTablero(request):
	listadotablero = Tablero.objects.all()
	contexto = {}
	contexto['objectlist'] = listadotablero
	return render(request, 'app1/consultarTablero.html', contexto)

def consultarLista(request):
	listadolista = Lista.objects.all()
	contexto = {}
	contexto['objectlist'] = listadolista
	return render(request, 'app1/consultarLista.html', contexto)

def consultarTarea(request):
	listadotarea = Tarea.objects.all()
	contexto = {}
	contexto['objectlist'] = listadotarea
	return render(request, 'app1/consultarTarea.html', contexto)