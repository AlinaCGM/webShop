from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from cart.models import Cart
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
