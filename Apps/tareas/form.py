from django import forms
# Create your views here.

from Apps.tareas.models import i00t_tareas

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
		'tx_descripcion': forms.TextInput(attrs={'class':'form-control'}),
		}