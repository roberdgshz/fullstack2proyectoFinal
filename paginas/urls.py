from django.urls import path
from .views import * # VistaBase, VistaEncabezado

urlpatterns = [
    path('', VistaInicio.as_view(), name="inicio"),
    path('base',VistaBase.as_view(), name="base"),
    path('enc',VistaEncabezado.as_view(), name="enc")
]