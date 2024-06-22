from django.db import models

# Create your models here.


class usuario (models.Model):
    nombreCuenta = models.CharField(max_length=20)
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    phoneNumber = models.CharField(max_length=30)
    direction = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

