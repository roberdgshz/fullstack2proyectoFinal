from django.views.generic import TemplateView

# Create your views here.
class VistaMonedas(TemplateView):
    template_name = 'paginas/monedas/index.html'