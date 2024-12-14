from django import forms
from .models import SubirArchivo

class SubirArchivoForm(forms.ModelForm):
    class Meta:
        model = SubirArchivo
        fields = ['name','file','description']