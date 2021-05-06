from django.urls import path
from.views import *

urlpatterns = [
    
    path('album/',vista_album, name='album_view'),
    path('ver_album/',vista_ver_album, name='ver_album_view'),

]