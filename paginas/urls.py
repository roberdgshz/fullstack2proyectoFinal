from django.urls import path
from .views import * # VistaBase, VistaEncabezado

urlpatterns = [
    path('', VistaInicio.as_view(), name="inicio"),
    path('monedas/index', VistaMonedas.as_view(), name="monedas_index"),
]