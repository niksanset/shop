from django.contrib import admin
from shop.models import Category, Product, CartItem, Cart

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)