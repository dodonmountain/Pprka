from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=10)

class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    preferenced_mall = models.CharField(max_length=5)
    wish_lists = models.ManyToManyField(Product, related_name='wish_users')
    REQUIRED_FIELDS = ['phone_number', 'email']

class OrderHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='buyers')
    created_at = models.DateTimeField(auto_now_add=True)