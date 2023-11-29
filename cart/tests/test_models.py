from django.test import TestCase

# Create your tests here.

from user.models import User_Model
from cart.models import Cart, CartItem
from product.models import Product
from datetime import date


class CartModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user on the class
        cls.user = User_Model.objects.create(
            email="testuser@example.com", username="testuser"
        )
        # Store user_id in a class variable so it easily can be refrenced in the tests
        cls.user_id = cls.user.user_id

    def test_created_at_timestamp_now(self):
        customer = User_Model.objects.get(user_id=self.user_id)
        cart = Cart.objects.create(user=customer)
        created_at = cart.created_at
        self.assertEqual(created_at, date.today())

    def test_get_absolute_url(self):
        customer = User_Model.objects.get(user_id=self.user_id)
        cart = Cart.objects.create(user=customer)
        self.assertEqual(cart.get_absolute_url(), "/cart/1/")


class CartItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user on the class
        cls.user = User_Model.objects.create(
            email="testuser@example.com", username="testuser"
        )
        # Store user_id in a class variable so it easily can be refrenced in the tests
        cls.user_id = cls.user.user_id

    def test_quantity_is_one_as_default(self):
        customer = User_Model.objects.get(user_id=self.user_id)
        cart = Cart.objects.create(user=customer)
        product = Product.objects.create(title="Tea cup", price="100")
        cartitem = CartItem(cart=cart, product=product)
        quantity = cartitem.quantity
        self.assertEqual(quantity, 1)

    def test_get_absolute_url(self):
        customer = User_Model.objects.get(user_id=self.user_id)
        cart = Cart.objects.create(user=customer)
        product = Product.objects.create(title="Tea cup", price="100")
        cartitem = CartItem(cart=cart, product=product)
        self.assertEqual(cartitem.get_absolute_url(), f"/cart/1/item/{cartitem.id}/")
