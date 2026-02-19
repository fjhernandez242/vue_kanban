from django.urls import re_path
from . import views

urlpatterns = [
    re_path('trabajos', views.trabajos),
    re_path('cargar', views.agregar_trabajo),
    re_path('posicion', views.cambiar_posicion),
    re_path('trabajo_id', views.getTrabajoById),
]
