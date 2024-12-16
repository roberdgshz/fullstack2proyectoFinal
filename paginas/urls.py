from django.urls import path
from .views import * # VistaBase, VistaEncabezado

urlpatterns = [
    path('', VistaInicio.as_view(), name="inicio"),
    path('/contacto', VistaContacto.as_view(), name="contacto"),
    path('/nosotros', VistaNosotros.as_view(), name='nosotros'),
    path('monedas/index', VistaMonedas, name="monedas_index"),
    path('monedas/<int:id>', VistaMonedaInfo, name="moneda_info")
]