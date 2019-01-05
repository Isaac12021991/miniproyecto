# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-01-05 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='i00t_tareas_estatus',
        ),
        migrations.RemoveField(
            model_name='i00t_tareas',
            name='co_usuario',
        ),
        migrations.RemoveField(
            model_name='i00t_tareas',
            name='ff_tarea',
        ),
        migrations.AlterField(
            model_name='i00t_tareas',
            name='co_estatus',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='i00t_tareas',
            name='in_activo',
            field=models.IntegerField(default=1),
        ),
    ]