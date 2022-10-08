# Generated by Django 4.1.1 on 2022-10-07 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import inventario.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.TextField(max_length=50)),
                ('primerApellido', models.TextField(max_length=50)),
                ('segundoApellido', models.TextField(max_length=50)),
                ('ci', models.TextField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('horaInicio', models.DateTimeField()),
                ('horaFin', models.DateTimeField()),
                ('description', models.TextField()),
                ('entradasDisponibles', models.IntegerField(validators=[inventario.validators.validar_mayor_a_cero])),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('clasificacion', models.CharField(choices=[('INF', 'Infantil'), ('ACC', 'Accion'), ('DOC', 'Documental'), ('ROM', 'Romance'), ('TP', 'Todo Público')], default='TP', max_length=3)),
                ('disponible', models.CharField(choices=[('nodisponible', 'No Disponible'), ('proximamente', 'Proximamente'), ('disponible', 'Disponible')], default='disponible', max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePelicula', models.CharField(max_length=100, unique=True, validators=[inventario.validators.validar_nombre_pelicula])),
                ('descripcion', models.TextField(max_length=100)),
            ],
            options={
                'permissions': [('reporte_cantidad', 'Visualizar el reporte de cantidad'), ('reporte_detalle', 'Reporte detallado de cantidades')],
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cantidadEntradas', models.IntegerField(default=0)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario_venta_cliente', to=settings.AUTH_USER_MODEL)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.horario')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario_venta_vendedor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='horario',
            name='pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.pelicula'),
        ),
    ]
