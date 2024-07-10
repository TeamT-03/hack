from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    parol = models.CharField(max_length=100, blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='products/')
