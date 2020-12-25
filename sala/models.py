from django.db import models

class Sala(models.Model):
    LIBRE = 'libre'
    OCUPADA = 'ocupada'
    STATUS_CHOICES = (
        (LIBRE, 'Libre'),
        (OCUPADA, 'Ocupada')
    )
    nombre = models.CharField(max_length=255)
    horarios = []
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=LIBRE)
