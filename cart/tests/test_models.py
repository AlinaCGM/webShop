from django.test import TestCase

# Create your tests here.

# from django.contrib.auth.models import User
from user.models import User_Model

from cart.models import Cart, CartItem
from product.models import Product
from datetime import date


class CartModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User_Model.objects.create(username="CustomerIAm")

    def test_created_at_timestamp_now(self):
        customer = User_Model.objects.get(id=1)
        cart = Cart.objects.create(user=customer)
        created_at = cart.created_at
        self.assertEqual(created_at, date.today())

    def test_get_absolute_url(self):
        customer = User_Model.objects.get(id=1)
        cart = Cart.objects.create(user=customer)
        self.assertEqual(cart.get_absolute_url(), "/cart/1/")


class CartItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User_Model.objects.create(username="CustomerIAm")

    def test_quantity_is_one_as_default(self):
        customer = User_Model.objects.get(id=1)
        cart = Cart.objects.create(user=customer)
        product = Product.objects.create(title="Tea cup", price="100")
        cartitem = CartItem(cart=cart, product=product)
        quantity = cartitem.quantity
        self.assertEqual(quantity, 1)

    def test_get_absolute_url(self):
        customer = User_Model.objects.get(id=1)
        cart = Cart.objects.create(user=customer)
        product = Product.objects.create(title="Tea cup", price="100")
        cartitem = CartItem(cart=cart, product=product)
        self.assertEqual(cartitem.get_absolute_url(), f"/cart/1/item/{cartitem.id}/")
