from django import forms
# Create your views here.

''' Importamos el model de tareas desde el models.py  '''

from Apps.tareas.models import i00t_tareas


''' Creamos la estructura del formulario Tareas, que lugo va a ser llamado desde views.py '''

class TareasForm(forms.ModelForm):

	class Meta:
		model = i00t_tareas

		fields = [
		'nb_tarea',
		'tx_descripcion',
		]
		labels = {
		'nb_tarea':'Tarea',
		'tx_descripcion': 'Descripcion',
		}
		widgets = {
		'nb_tarea': forms.TextInput(attrs={'class':'form-control'}),
		'tx_descripcion': forms.Textarea(attrs={'class':'form-control'}),
		}