from django.test import TestCase
from django.test import Client
from .models import Pelicula
from django.core.exceptions import ValidationError
from django.test import tag


class TestPeliculas(TestCase):
    def setUp(self):
        self.client = Client()
        Pelicula.objects.create(nombrePelicula="Pelicula 1")
        Pelicula.objects.create(nombrePelicula="Pelicula 2")

    def test_grabacion_peliculas(self):
        q = Pelicula(nombrePelicula="Pelicula 5")
        q.save()
        self.assertEqual(Pelicula.objects.count(), 3)

    @tag('validacion')
    def test_grabacion_peliculas_no_permitido(self):
        q = Pelicula.objects.create(nombrePelicula="No permitido")
        self.assertRaises(ValidationError, q.full_clean)

    @tag('validacion')
    def test_grabacion_peliculas_no_permitido_mensaje(self):
        with self.assertRaises(ValidationError) as qv:
            q = Pelicula.objects.create(nombrePelicula="No permitido")
            q.full_clean()

        mensaje_error = dict(qv.exception)
        self.assertEqual(mensaje_error["nombrePelicula"][0], "No es una opcion permitida")

    def test_pelicula_listo(self):
        response = self.client.get('/inventario/peliculas/')
        self.assertContains(response, "Pelicula 1", status_code=200, html=True)

    def test_pelicula_filtro(self):
        response = self.client.get('/inventario/peliculas/?nombrePelicula=Pelicula 2')
        self.assertNotContains(response, "Pelicula 1", status_code=200, html=True)

    def test_pelicula_formulario(self):
        response = self.client.post('/inventario/peliculas/', {"nombrePelicula": "Pelicula 3"})
        self.assertContains(response, "Pelicula 3", status_code=200, html=True)

