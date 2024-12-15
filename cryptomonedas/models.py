from django.db import models

# Create your models here.
class Monedas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    nameKey = models.CharField(max_length=5)
    value = models.FloatField()

    def __str__(self):
        return self.name