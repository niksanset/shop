from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category/', default='category/default.jpg')


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product/', default='product/default.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    is_paid = models.BooleanField(default=False)
