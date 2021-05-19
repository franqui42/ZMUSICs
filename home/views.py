from django.shortcuts import render,redirect
from.forms import *
from.models import *
# Create your views here.


def vista_album(request):
    album = Album.objects.filter()
    return render(request, 'album.html',locals())

def vista_ver_album(request,id_alb):
    detalle =Album.objects.get(id=id_alb)
    return render(request, 'ver_album.html',locals())

def vista_inicio(request):
    return render(request, 'inicio.html',locals())

def agregar_album (request):

    if request.method=='POST':
        formulario= agregar_album_form(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/album/')
    else:
        formulario=agregar_album_form()

        return render(request, 'agregar_album.html',locals())

def vista_editar(request,id_alb):
    objeto =Album.objects.get(id=id_alb)
    if request.method == 'POST':
        formulario= agregar_album_form(request.POST, request.FILE,instance=objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/albums/')
    else:
        formulario = agregar_album_form(instance=objeto)
    return render(request, 'agregar_album.html',locals())

def vista_conoce(request):
    return render(request, 'conoce.html',locals())