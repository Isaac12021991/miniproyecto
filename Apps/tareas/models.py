from django.db import models

# Create your models here.

class i00t_tareas(models.Model):
	co_estatus = models.IntegerField(default=1)
	nb_tarea = models.CharField(max_length=50)
	tx_descripcion = models.CharField(max_length=200)
	in_activo = models.IntegerField(default=1)