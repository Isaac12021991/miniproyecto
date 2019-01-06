from django.conf.urls import url, include

''' Importa todas las vistas a utilizar desde el views.py, es decir todas las funciones que se encuentran en ella  '''

from Apps.tareas.views import index, tareas_view, tareas_lista_view, tareas_aprobar


''' Establecemos todas las urls disponibles para la Apps Tareas  '''

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nueva_tarea$', tareas_view, name='nombre_tareas_form'),
    url(r'^listar_tareas$', tareas_lista_view, name='nombre_tareas_listar'),
    url(r'^aprobar_tareas/(?P<id_tarea>\d+)/$', tareas_aprobar, name='nombre_aprobar_tareas'),
]
