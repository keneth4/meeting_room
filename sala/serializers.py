from rest_framework import serializers
from .models import Sala

class SalaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sala
        fields = ('id', 'nombre', 'status', 'horarios')
