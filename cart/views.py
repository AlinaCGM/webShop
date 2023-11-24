from django.shortcuts import render

# Create your views here.

from .models import Cart, CartItem


def cart_view(request):
    num_carts = Cart.objects.all().count()

    render(request, "cart.html", context={"num_carts": num_carts})
