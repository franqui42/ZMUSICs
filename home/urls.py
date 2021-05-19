from django.urls import path
from.views import *

urlpatterns = [

    path('',vista_inicio, name='inicio_view'),
    path('album/',vista_album, name='album_view'),
    path('ver_album/<int:id_alb>',vista_ver_album, name='ver_album_view'),
    path('agregar_album/',agregar_album, name='agregar_album_view'),
    path('conoce/',vista_conoce, name='conoce_view'),

    path('editar/<int:id_alb>',vista_editar, name='editar_view'),

]