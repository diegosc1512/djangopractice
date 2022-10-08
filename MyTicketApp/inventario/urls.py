from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"peliculas", views.PeliculaViewSet)


urlpatterns = [
    # path('contacto/<str:nombre>', views.contacto, name='contacto'),
    # path('', views.index, name='index'),
    path('mensaje/enviar', views.enviar_mensaje),
    
    path('horarios/', views.HorarioFormView, name='horarios'),
    path('horarios/reporte', views.reporte_horarios),
    path('horarios/create_list', views.HorarioCreateAndList.as_view(), name='horarios'),

    path('peliculas/', views.peliculaFormView, name='peliculas'),
    path('peliculas/cantidad', views.pelicula_cantidad),
    path('peliculas/reporte', views.reporte_peliculas),
    path('peliculas/create_list', views.PeliculaCreateAndList.as_view(), name='peliculas'),
    path('peliculas/tipo/clasificacion', views.peliculas_tipo_clasificacion),

    path('clientes/', views.ClienteFormView, name='clientes'),
    path('clientes/reporte', views.reporte_clientes),
    path('clientes/create_list', views.ClienteCreateAndList.as_view(), name='clientes'),

    path('ventas/', views.VentaFormView, name='ventas'),
    path('ventas/reporte', views.reporte_ventas),
    path('ventas/create_list', views.VentaCreateAndList.as_view(), name='ventas'),
  
    path('', include(router.urls))
]
