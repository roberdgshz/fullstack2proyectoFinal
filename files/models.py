from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SubirArchivo(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"