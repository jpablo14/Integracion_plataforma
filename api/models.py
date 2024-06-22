from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombreempresa = models.CharField(max_length=100)
    rutempresa = models.CharField(max_length=12)
    direccion = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)