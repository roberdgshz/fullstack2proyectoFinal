from django.views.generic import TemplateView
from django.shortcuts import render,get_object_or_404
from cryptomonedas.models import Monedas

class VistaInicio(TemplateView):
    template_name = 'paginas/inicio.html'

class VistaContacto(TemplateView):
    template_name = 'paginas/contacto.html'

class VistaNosotros(TemplateView):
    template_name = 'paginas/nosotros.html'

def VistaMonedas(request):
    monedas = Monedas.objects.all()
    return render(request, 'paginas/monedas/index.html', {'monedas': monedas})
    
def VistaMonedaInfo(request, id):
    moneda = get_object_or_404(Monedas, id=id)
    return render(request, 'paginas/monedas/moneda_info.html', {'moneda': moneda})

# página de iniciar sesión
# página de registrarse 
