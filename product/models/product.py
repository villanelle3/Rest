# models product
from django.db import models
from product.models import Category

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)  # on_delete=models.CASCADE
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.FloatField(null = True)
    active = models.BooleanField(default = True)
    categories = models.ManyToManyField(Category, blank=True)
    def __str__(self):
        return f"Produto: {self.title}."