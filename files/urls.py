from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.Subir_Archivo, name='upload_file'),
    path('files/', views.file_list, name="file_list"),
    path('comments/add/', views.add_comment, name='add_comment'),
    path('comments/', views.comment_list, name='comment_list'),
]