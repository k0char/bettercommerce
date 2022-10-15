from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.db import models
#michaladmin / michal123

class User(AbstractUser):
    pass
class Category(models.Model):
    categoryName = models.CharField(max_length=50)

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    imageURL = models.CharField(max_length=1000)
    price = models.FloatField()
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")