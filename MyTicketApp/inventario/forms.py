from django import forms

from .models import  Pelicula, Horario, Cliente, Venta


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = "__all__"

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = "__all__"
