from rest_framework import fields, serializers
from home.models import *

class album_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('url','artista','nombre','descripcion','año','foto','genero')

class genero_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genero
        fields = ('url','nombre','descripcion')

