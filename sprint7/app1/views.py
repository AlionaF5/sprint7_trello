from django.shortcuts import render,redirect,get_list_or_404
from django.forms import ModelForm
from app1.models import Tablero,Lista,Tarea

# Create your views here.
def home(request):
    return render(request,'app1/base.html',{})
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
        return redirect('consultarTablero')
    return render(request,plantilla,{'form':form})

def crearLista(request):
    plantilla='app1/crearLista.html'
    form=ListaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('consultarLista')
    return render(request,plantilla,{'form':form})

def crearTarea(request):
    form=TareaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'app1/crearTarea.html',{'form':form})

def consultarTablero(request):
    template='app1/consultarTablero.html'
    listadoTablero=Tablero.objects.all()
    contexto={}
    contexto['object_list']=listadoTablero
    return render(request,template,contexto)

def consultarLista(request):
    template='app1/consultarLista.html'
    listadoLista=Lista.objects.all()
    contexto={}
    contexto['object_list']=listadoLista
    return render(request,template,contexto)

def consultarTarea(request):
    template='app1/consultarTarea.html'
    listadoTarea=Tarea.objects.all()
    contexto={}
    contexto['object_list']=listadoTarea
    return render(request,template,contexto)



