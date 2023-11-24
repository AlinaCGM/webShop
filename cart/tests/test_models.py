from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from django.utils import timezone


class CartModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="CustomerIAm")

    def test_created_at_timestamp_now(self):
        customer = User.objects.get(id=1)
        created_at = customer["created_at"]
        self.assertEqual(created_at, timezone.localtime())
