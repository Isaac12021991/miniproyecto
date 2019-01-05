from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.tareas.form import TareasForm
from Apps.tareas.models import i00t_tareas

# Create your views here.

def index(request):
	return render(request, 'tareas/index.html')

def tareas_view(request):
	if request.method == 'POST':
		form = TareasForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('tareas:nombre_tareas_listar')
	else:
		form = TareasForm()
	return render(request, 'tareas/tareas_form.html', {'form':form})

def tareas_lista_view(request):
	tareas = i00t_tareas.objects.all()
	data = {'lista_tareas':tareas}
	return render(request, 'tareas/listar_tareas.html', data)

def tareas_aprobar(request, id_tarea):
	query = i00t_tareas.objects.get(id=id_tarea)
	if request.method == 'POST':
		co_estatus = '2';
		query.co_estatus = co_estatus
		query.save()
		return redirect('tareas:nombre_tareas_listar')
	return render(request, 'tareas/tareas_aprobar.html', {'info_tarea':query})