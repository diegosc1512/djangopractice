# Generated by Django 4.1.1 on 2022-10-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='clasificacion',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='clasificacion',
            field=models.CharField(choices=[('INF', 'Infantil'), ('ACC', 'Accion'), ('DOC', 'Documental'), ('ROM', 'Romance'), ('TP', 'Todo Público')], default='TP', max_length=3),
        ),
    ]
