from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Horario, Cliente,  Venta
from .models import Pelicula
from .forms import HorarioForm, ClienteForm, PeliculaForm, VentaForm

from .serializers import PeliculaSerializer
from .serializers import ClienteSerializer
from .serializers import HorarioSerializer
from .serializers import VentaSerializer
from .serializers import ContactSerializer

from .serializers import ReportePeliculasSerializer
from .serializers import ReporteHorariosSerializer
from .serializers import ReporteClientesSerializer
from .serializers import ReporteVentasSerializer

from .permissions import IsSuperUser
#from .utils import permission_required
import logging


logger = logging.getLogger(__name__)
logger = logging.getLogger("Nombre personalizado")

def index(request):
    return HttpResponse("Hola Mundo")

def contacto(request, nombre):
    return HttpResponse(f"Bienvenido {nombre} a la clase de Django")

def peliculaFormView(request):
    post_nombre = request.POST.get('nombrePelicula')
    if post_nombre:
        q = Pelicula(nombrePelicula=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombrePelicula")
    if filtro_nombre:
        peliculas = Pelicula.objects.filter(nombre__contains=filtro_nombre)
    else:
        peliculas = Pelicula.objects.all()
    print(peliculas.query)
    return render(request, "peliculas.html", {"peliculas": peliculas})

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    #permission_classes = [IsSuperUser]  #Para Validar SuperUsuario

#@permission_classes([IsAuthenticated])
class PeliculaCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


def HorarioFormView(request):
    form = HorarioForm()
    horario = None
    
    id_horario = request.GET.get('id')
    if id_horario:
        horario = get_object_or_404(Horario, id=id_horario)
        form = HorarioForm(instance=horario)

    if request.method == 'POST':
        if horario:
            form = HorarioForm(request.POST, instance=horario)
        else:
            form = HorarioForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "horarios.html", {"form": form})

def ClienteFormView(request):
    form = ClienteForm()
    cliente = None
    
    id_cliente = request.GET.get('id')
    if id_cliente:
        cliente = get_object_or_404(Cliente, id=id_cliente)
        form = ClienteForm(instance=cliente)

    if request.method == 'POST':
        if cliente:
            form = ClienteForm(request.POST, instance=cliente)
        else:
            form = ClienteForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "clientes.html", {"form": form})

def VentaFormView(request):
    form = VentaForm()
    venta = None
    
    id_venta = request.GET.get('id')
    if id_venta:
        venta = get_object_or_404(Venta, id=id_venta)
        form = VentaForm(instance=venta)

    if request.method == 'POST':
        if venta:
            form = VentaForm(request.POST, instance=venta)
        else:
            form = VentaForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "horarios.html", {"form": form})



class HorarioCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class ClienteCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VentaCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

@api_view(["GET"])
def pelicula_cantidad(request):
    """
    Cantidad de items en el modelo pelicula
    """
    logger.info("Cantidad pelicula mostrada correctamente")
    try:
        cantidad = Pelicula.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def peliculas_tipo_clasificacion(request):
    """
    Peliculas filtradas por clasificacion
    """
    try:
        peliculas = Pelicula.objects.filter(clasificacion='TP')
        return JsonResponse(
            PeliculaSerializer(peliculas, many=True).data,
            safe=False,
            status=200,
        ) 
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def reporte_horarios(request):
    """
    Reporte de horarios
    """
    try:
        horarios = Horario.objects.all()
        cantidad = horarios.count()

        return JsonResponse(
            ReporteHorariosSerializer({
                "cantidad": cantidad,
                "horarios": horarios
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def reporte_clientes(request):
    """
    Reporte de clientes
    """
    try:
        clientes = Cliente.objects.all()
        cantidad = clientes.count()

        return JsonResponse(
            ReporteClientesSerializer({
                "cantidad": cantidad,
                "clientes": clientes
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def reporte_ventas(request):
    """
    Reporte de ventas
    """
    try:
        ventas = Venta.objects.all()
        cantidad = ventas.count()

        return JsonResponse(
            ReporteVentasSerializer({
                "cantidad": cantidad,
                "ventas": ventas
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def reporte_peliculas(request):
    """
    Reporte de peliculas
    """
    try:
        peliculas = Pelicula.objects.all()
        cantidad = peliculas.count()

        return JsonResponse(
            ReportePeliculasSerializer({
                "cantidad": cantidad,
                "peliculas": peliculas
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["POST"])
def enviar_mensaje(request):
    """
    Enviar mensajes via email
    """
    cs = ContactSerializer(data=request.data)
    if cs.is_valid():
        return JsonResponse({"mensaje": "Mensaje enviado satisfactoriamente"}, status=200)
    else:
        return JsonResponse({"mensaje": cs.errors}, status=200)

