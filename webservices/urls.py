from django.urls import path, include
from rest_framework import routers
from home.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'albums',album_viewset)
router.register(r'generos',genero_viewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]