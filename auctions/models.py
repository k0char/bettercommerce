from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
class Categories(models.Model):
    name = models.CharField(max_length=30)