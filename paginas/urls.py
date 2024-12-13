from django.urls import path
from .views import * # VistaBase, VistaEncabezado

urlpatterns = [
    path('', VistaInicio.as_view(), name="inicio"),
]