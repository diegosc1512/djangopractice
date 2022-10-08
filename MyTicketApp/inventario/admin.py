from django.contrib import admin
from .models import Pelicula
from .models import Horario
from .models import Venta
from .models import Cliente


class HorarioAdmin(admin.ModelAdmin):
    list_display = ("fecha", "horaInicio", "horaFin", "entradasDisponibles", "disponible")
    ordering = ["fecha"]
    search_fields = ["fecha", "horaInicio", "horaFin"]
    list_filter = ("fecha", "horaInicio", "horaFin", "entradasDisponibles")


admin.site.register(Pelicula)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Venta)
admin.site.register(Cliente)
