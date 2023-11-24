from django.db import models

# Create your models here.


# Placeholder for the Product model
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
