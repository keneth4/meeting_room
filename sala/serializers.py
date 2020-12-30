from rest_framework import serializers
from .models import Sala

# Serializador que nos ayudará a enviar y recibir información entre la API y el sitio web en formato JSON
class SalaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sala
        fields = ('id', 'nombre', 'status', 'horarios')