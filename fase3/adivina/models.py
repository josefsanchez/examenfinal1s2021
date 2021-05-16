from django.db import models

# Create your models here.

class Juego (models.Model):
    nombre  = models.CharField(max_length=50)
    numero  = models.IntegerField()
    intento = models.IntegerField()

