from django.shortcuts import render

from home.models import *
from .serializer import *
from rest_framework import viewsets
# Create your views here.

class album_viewset (viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = album_serializer

class genero_viewset (viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = genero_serializer