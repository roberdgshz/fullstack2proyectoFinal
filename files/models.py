from django.db import models

# Create your models here.

class SubirArchivo(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
