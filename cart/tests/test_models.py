from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from product.models import Product
from django.utils import timezone


class CartModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="CustomerIAm")

    def test_created_at_timestamp_now(self):
        customer = User.objects.get(id=1)
        cart = Cart.objects.create(user=customer)
        created_at = cart.created_at
        self.assertEqual(created_at, timezone.now())


class CartItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="CustomerIAm")

    def test_quantity_is_one_as_default(self):
        customer = User.objects.get(id=1)
        cart = Cart.objects.create(user=customer)
        product = Product.objects.create(title="Tea cup", price="100")
        cartitem = CartItem(cart=cart, product=product)
        quantity = cartitem.quantity
        self.assertEqual(quantity, 1)
