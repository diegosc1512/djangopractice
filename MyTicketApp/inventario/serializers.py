from rest_framework import serializers
from .models import Pelicula
from .models import Horario
from .models import Venta
from .models import Cliente
from .validators import validar_nombre_subject 

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = "__all__"

class ReportePeliculasSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    peliculas = PeliculaSerializer(many=True)

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = "__all__"


class ReporteHorariosSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    horarios = HorarioSerializer(many=True)

class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=100, validators=[validar_nombre_subject,])
    body = serializers.CharField(max_length=255)

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = "__all__"

class ReporteVentasSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    ventas = VentaSerializer(many=True)

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = "__all__"    

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class ReporteClientesSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    clientes = ClienteSerializer(many=True)

