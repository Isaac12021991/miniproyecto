from django.shortcuts import render, redirect
from django.http import HttpResponse

''' Importa los datos del formulario desde App.tareas.form.py '''

from Apps.tareas.form import TareasForm

''' Importa el modelo de datos desde el models.py, que este caso es i00_tareas '''

from Apps.tareas.models import i00t_tareas

# Create your views here.


''' Carga de forma predeteminada el index.html del sitio '''

def index(request):
	return render(request, 'tareas/index.html')


''' Funcion que permite registrar una nueva tarea, solicitando a traves de TareaForm, que fue la carga del
model importado, los campos necesarios para realizar el registro de una nueva tarea'''

def tareas_view(request):
	if request.method == 'POST':
		form = TareasForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('tareas:nombre_tareas_listar')
	else:
		form = TareasForm()
	return render(request, 'tareas/tareas_form.html', {'form':form})


''' Funcion que permite la carga de la vista de todas las tareas registradas por el usuario '''

def tareas_lista_view(request):
	tareas = i00t_tareas.objects.all()
	data = {'lista_tareas':tareas}
	return render(request, 'tareas/listar_tareas.html', data)


''' La siguiente funcion aprueba una tarea, cargando la identificacion de la tarea por medio del id, se establecera de la siguiente manera:

co_estatus = 1: indica que la tarea es nueva y esta pendiente.
co_estatus = 2: indica que la tarea ya ha sido aprobada.

En esta funcion el co_estatus se establece en co_estatus = 2, como podemos observar en la linea de codigo Nro 54
'''

def tareas_aprobar(request, id_tarea):
	query = i00t_tareas.objects.get(id=id_tarea)
	if request.method == 'POST':
		co_estatus = '2';
		query.co_estatus = co_estatus
		query.save()
		return redirect('tareas:nombre_tareas_listar')
	return render(request, 'tareas/tareas_aprobar.html', {'info_tarea':query})