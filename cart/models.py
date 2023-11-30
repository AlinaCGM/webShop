from django.db import models

# # Create your models here.

from user.models import User_Model
from product.models import Product
from django.urls import reverse
from django.utils import timezone


class Cart(models.Model):
    """Model representing a users cart"""

    # A User can only have one Cart and a Cart can only belong to one User
    # When the User referencing the Cart is deleted, the associated Cart will also be deleted
    user = models.OneToOneField(User_Model, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, null=False)

    def cart_total_price(self):
        # FIX colculate this here or in the template based on total_price of each item
        pass

    def get_absolute_url(self):
        """Return the URL to access a particular cart instance"""
        return reverse("cart", args=[str(self.id)])

    def __str__(self):
        return f"Customer: {self.user.email} (id: {self.user.user_id})"


import uuid


class CartItem(models.Model):
    """Model representing an item in a cart (an item in a cart can actually have its quantity increased by the user)"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )

    # A CartItem can have one and only one Cart (not 0 or many), but a Cart can have 0 or many CartItems
    # When the Cart referencing the CartItem is deleted, the associated CartItem will also be deleted
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=False)

    # A CartItem can have one and only one Product, but a Product can have 0 or many CartItems
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_to_cart = models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        ordering = ["added_to_cart"]

    def total_price(self):
        return self.quantity * self.product.price

    def get_absolute_url(self):
        return reverse("cartitem-detail", args=[str(self.cart.id), str(self.id)])

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"
