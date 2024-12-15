from django.shortcuts import render, redirect
from .forms import SubirArchivoForm, CommentForm
from .models import SubirArchivo, Comment
from django.contrib.auth.decorators import login_required

# Búsquedas
from django.db.models import Q

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

@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'files/add_comment.html', {'form': form})

def comment_list(request):
    query = request.GET.get('q')
    if query:
        comments = Comment.objects.filter(
            Q(content__icontains=query) | Q(user__username__icontains=query)
        ).order_by('-created_at')
    else:
        comments = Comment.objects.order_by('-created_at')

    return render(request, 'files/comment_list.html', {'comments': comments, 'query': query})