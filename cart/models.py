from django.db import models

# Create your models here.


class Cart(models.model):
    """Model representing users cart"""

    # A user can have only one cart and a cart can only belong to one user, so the records in the cart table always need a Unique user foreign key
    # on_delete=models.RESTRICT prevents the carts associated user being deleted if it is referenced by any cart
    user = models.ForeignKey("User", on_delete=models.RESTRICT, null=False, unique=True)

    # Can have multiple carditems

    def get_absolute_path(self):
        pass


class CartItem(models.model):
    """Model representing an item in a cart"""

    # Can only have one cart
    cart = models.ForeignKey("Cart", on_delete=models.RESTRICT, null=False)

    # Can have multiple instances of a product
