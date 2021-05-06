from django.shortcuts import render
from.forms import *
from.models import *
# Create your views here.


def vista_album(request):
    album = Album.objects.filter()

    return render(request, 'album.html',locals())

def vista_ver_album(request):

    return render(request, 'ver_album.html',locals())