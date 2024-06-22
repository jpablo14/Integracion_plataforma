from django.db import models

# Create your models here.


class products(models.Model):
    productName = models.CharField(max_length=100)
    brandName = models.CharField(max_length=50)
    stock = models.PositiveSmallIntegerField()
    codeProduct = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
