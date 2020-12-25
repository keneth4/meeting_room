from django.shortcuts import render
from .models import Sala
from .serializers import SalaSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SalaViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
