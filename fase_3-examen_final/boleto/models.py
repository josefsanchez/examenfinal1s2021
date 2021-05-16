from django.db import models

# Create your models here.

class Boleto (models.Model):
    subtotal    = models.DecimalField(max_digits=8, decimal_places=2)
    desc        = models.IntegerField()
    total       = models.DecimalField(max_digits=8, decimal_places=2)
