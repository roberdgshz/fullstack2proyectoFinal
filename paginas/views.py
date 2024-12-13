from django.views.generic import TemplateView

class VistaBase(TemplateView):
    template_name = 'base.html'

class VistaEncabezado(TemplateView):
    template_name = 'encabezado.html'

class VistaInicio(TemplateView):
    template_name = 'inicio.html'