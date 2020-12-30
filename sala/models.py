from django.db import models

# Modelo que define la estructura de la base de datos para las salas
class Sala(models.Model):
    LIBRE = 'libre'
    OCUPADA = 'ocupada'
    STATUS_CHOICES = (
        (LIBRE, 'Libre'),
        (OCUPADA, 'Ocupada')
    )
    nombre = models.CharField(max_length=255) # Columna de nombre de la sala
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=LIBRE) # Columna de status de la sala
    horarios = models.TextField(blank=True) # Columna de Array de horarios que será almacenado en formato JSON en texto puro
