from django.core.exceptions import ValidationError

def validar_mayor_a_cero(value):
    if value <= 0:
        raise ValidationError(
            '%(value)s no hay entradas disponibles',
            params={'value': value}
        )

def validar_nombre_pelicula(value):
    if value == '':
        raise ValidationError("El nombre no puede ser vacío")

def validar_nombre_subject(value):
    if value == 'Ninguno':
        raise ValidationError("No es una opcion permitida")
