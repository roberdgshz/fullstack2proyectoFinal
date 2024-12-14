from django.shortcuts import render, redirect
from .forms import SubirArchivoForm
from .models import SubirArchivo

# Create your views here.
def Subir_Archivo(request):
    if request.method == 'POST':
        form = SubirArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = SubirArchivoForm()
    return render(request, 'files/upload.html', {'form': form})

def file_list(request):
    files = SubirArchivo.objects.all()
    return render(request, 'files/file_list.html', {'files': files})