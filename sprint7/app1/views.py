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

def consultarLista(request, id):
	listadolista = Lista.objects.filter(fk_tablero_id=id)
	contexto = {}
	contexto['objectlist'] = listadolista
	return render(request, 'app1/consultarLista.html', contexto)

def consultarTarea(request, id):
	listadotarea = Tarea.objects.filter(fk_lista_id=id)
	contexto = {}
	contexto['objectlist'] = listadotarea
	return render(request, 'app1/consultarTarea.html', contexto)

def modificarTablero(request,id):
	template = 'app1/crearTablero.html'#el template al q me va a llamar a esta lista
	info_tablero = get_object_or_404(Tablero,pk=id)#coger informacion, me da una inf de 404 si no encuentra
	form = TableroForm(request.POST or None, instance= info_tablero)#como no me interesa un formulario vacio, tengo q decirle q me la llene con un cliente 
	
	if form.is_valid():
		form.save()
		return redirect('consultarTablero')#lo redirecciono, el nombre de la ruta corresponde al nombre del name del url
	return render(request,template,{'form':form})

def modificarLista(request,id):
	template = 'app1/crearLista.html'#el template al q me va a llamar a esta lista
	info_lista = get_object_or_404(Lista,pk=id)#coger informacion, me da una inf de 404 si no encuentra
	form = ListaForm(request.POST or None, instance= info_lista)#como no me interesa un formulario vacio, tengo q decirle q me la llene con un cliente 
	
	if form.is_valid():
		form.save()
		return redirect('consultarLista')#lo redirecciono, el nombre de la ruta corresponde al nombre del name del url
	return render(request,template,{'form':form})

def modificarTarea(request,id):
	template = 'app1/crearTarea.html'#el template al q me va a llamar a esta lista
	info_tarea = get_object_or_404(Tarea,pk=id)#coger informacion, me da una inf de 404 si no encuentra
	form = TareaForm(request.POST or None, instance= info_tarea)#como no me interesa un formulario vacio, tengo q decirle q me la llene con un cliente 
	
	if form.is_valid():
		form.save()
		return redirect('consultarTarea')#lo redirecciono, el nombre de la ruta corresponde al nombre del name del url
	return render(request,template,{'form':form})

def eliminarTablero(request,id):
	template = 'app1/confElimTablero.html'
	idtablero = get_object_or_404(Tablero,pk=id)
	if request.method == 'POST':
		idtablero.delete()
		return redirect('consultarTablero')
	return render(request,template,{'idtablero':idtablero})

def eliminarLista(request,id):
	template = 'app1/confElimLista.html'
	idlista = get_object_or_404(Lista,pk=id)
	if request.method == 'POST':
		idlista.delete()
		return redirect('consultarLista')
	return render(request,template,{'idlista':idlista})

def eliminarTarea(request,id):
	template = 'app1/confElimTarea.html'
	idtarea = get_object_or_404(Tarea,pk=id)
	if request.method == 'POST':
		idtarea.delete()
		return redirect('consultarTarea')
	return render(request,template,{'idtarea':idtarea})