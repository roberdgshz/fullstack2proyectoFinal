from django import forms
from .models import SubirArchivo, Comment

class SubirArchivoForm(forms.ModelForm):
    class Meta:
        model = SubirArchivo
        fields = ['name','file','description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Comenta aquí'}),
        }