from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.forms import ModelForm
from app1.models import Tablero,Lista,Tarea

# Create your views here.
def home(request):
    return render(request,'app1/base.html',{})
def tablerocreado(request):
    return render(request,'app1/tablerocreado.html',{})

def listacreada(request):
    return render(request,'app1/listacreada.html',{})

def tareacreada(request):
    return render(request,'app1/tareacreada.html',{})

def salir(request):
    return render(request,'app1/salir.html',{})

class TableroForm(ModelForm):
    class Meta:
        model =Tablero
        fields=['nombre_tablero']

class ListaForm(ModelForm):
    class Meta:
        model=Lista
        fields=['nombre_lista','fk_tablero']   
        
class TareaForm(ModelForm):
    class Meta:
        model=Tarea
        fields=['nombre_tarea','descripcion','fk_lista']

def crearTablero(request):
    plantilla='app1/crearTablero.html'
    form=TableroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tablerocreado')
    return render(request,plantilla,{'form':form})

def crearLista(request):
    plantilla='app1/crearLista.html'
    form=ListaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listacreada')
    return render(request,plantilla,{'form':form})

def crearTarea(request):
    form=TareaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tareacreada')
    return render(request, 'app1/crearTarea.html',{'form':form})

def consultarTablero(request):
    template='app1/consultarTablero.html'
    listadoTablero=Tablero.objects.all()
    contexto={}
    contexto['object_list']=listadoTablero
    return render(request,template,contexto)

def consultarLista(request,id):
    template='app1/consultarLista.html'
    listadoLista = Lista.objects.filter(fk_tablero_id=id)
    contexto={}
    contexto['object_list']=listadoLista
    return render(request,template,contexto)

def consultarTarea(request,id):
    template='app1/consultarTarea.html'
    listadoTarea = Tarea.objects.filter(fk_lista_id=id)
    contexto={}
    contexto['object_list']=listadoTarea
    return render(request,template,contexto)

def editarTablero(request,id):
	template = 'app1/crearTablero.html'#el template al q me va a llamar a esta lista
	info_tablero = get_object_or_404(Tablero,pk=id)#coger informacion, me da una inf de 404 si no encuentra
	form = TableroForm(request.POST or None, instance= info_tablero)#como no me interesa un formulario vacio, tengo q decirle q me la llene con un cliente 
	
	if form.is_valid():
		form.save()
		return redirect('consultarTablero')#lo redirecciono, el nombre de la ruta corresponde al nombre del name del url
	return render(request,template,{'form':form})

def editarLista(request,id):
	template = 'app1/crearLista.html'#el template al q me va a llamar a esta lista
	info_lista = get_object_or_404(Lista,pk=id)#coger informacion, me da una inf de 404 si no encuentra
	form = ListaForm(request.POST or None, instance= info_lista)#como no me interesa un formulario vacio, tengo q decirle q me la llene con un cliente 
	
	if form.is_valid():
		lista=form.save()
        
		return redirect('consultarLista',lista.fk_tablero.id)#lo redirecciono, el nombre de la ruta corresponde al nombre del name del url
	return render(request,template,{'form':form})

def editarTarea(request,id):
	template = 'app1/crearTarea.html'#el template al q me va a llamar a esta lista
	info_tarea = get_object_or_404(Tarea,pk=id)#coger informacion, me da una inf de 404 si no encuentra
	form = TareaForm(request.POST or None, instance= info_tarea)#como no me interesa un formulario vacio, tengo q decirle q me la llene con un cliente 
	
	if form.is_valid():
		tarea=form.save()
		return redirect('consultarTarea',tarea.fk_lista.id)#lo redirecciono, el nombre de la ruta corresponde al nombre del name del url
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
		return redirect('consultarLista',idlista.fk_tablero.id)
	return render(request,template,{'idlista':idlista})

def eliminarTarea(request,id):
	template = 'app1/confElimTarea.html'
	idtarea = get_object_or_404(Tarea,pk=id)
	if request.method == 'POST':
		idtarea.delete()
		return redirect('consultarTarea',idtarea.fk_lista.id)
	return render(request,template,{'idtarea':idtarea})


