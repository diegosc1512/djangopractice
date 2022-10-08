from tkinter import DISABLED
from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings
from .validators import validar_mayor_a_cero 
from .validators import validar_nombre_pelicula 
# from django.core.validators import EmailValidator 

class ClasificacionPeliculas(models.TextChoices):
    INF = 'INF', 'Infantil'
    ACC = 'ACC', 'Accion'
    DOC = 'DOC', 'Documental'
    ROM = 'ROM', 'Romance'
    TP = 'TP','Todo Público'

class Pelicula(models.Model):
    nombrePelicula = models.CharField(max_length=100, unique=True, validators=[validar_nombre_pelicula,]) 
    descripcion = models.TextField(max_length=100)
    clasificacion = models.CharField(
        max_length = 3,
        choices = ClasificacionPeliculas.choices,
        default = ClasificacionPeliculas.TP
    )
    def __str__(self):
        return self.nombrePelicula

    class Meta:
        permissions = [
            ("reporte_cantidad", "Visualizar el reporte de cantidad"),
            ("reporte_detalle", "Reporte detallado de cantidades"),
        ]

class EstadoDisponibilidad(models.TextChoices):
    NODISPONIBLE = 'nodisponible', 'No Disponible'
    PROXIMAMENTE = 'proximamente', 'Proximamente'
    DISPONIBLE = 'disponible', 'Disponible'

class Horario(models.Model):
    fecha = models.DateField()
    horaInicio = models.DateTimeField()
    horaFin = models.DateTimeField() 
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE) 
    description = models.TextField()
    entradasDisponibles = models.IntegerField(validators=[validar_mayor_a_cero,])
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    disponible = models.CharField(
        max_length = 15,
        choices = EstadoDisponibilidad.choices,
        default = EstadoDisponibilidad.DISPONIBLE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Horario - %s" % self.fecha

    
class Venta(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inventario_venta_cliente"
    )
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE) 
    cantidadEntradas = models.IntegerField(default=0)
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inventario_venta_vendedor"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Cliente(models.Model):
    nombres = models.TextField(max_length=50)
    primerApellido = models.TextField(max_length=50)
    segundoApellido = models.TextField(max_length=50)
    ci = models.TextField(max_length=15)
    email = models.EmailField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    

