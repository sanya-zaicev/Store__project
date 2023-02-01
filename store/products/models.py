from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
