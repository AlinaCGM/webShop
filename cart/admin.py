from django.contrib import admin

# Register your models here.

from product.models import Product
from .models import Cart, CartItem

#admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
