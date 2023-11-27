from django.shortcuts import render

# Create your views here.

from .models import Cart, CartItem
from django.shortcuts import get_object_or_404


def cart(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    cart_user = cart.user
    num_carts_total = Cart.objects.all().count()

    context = {"cart_user": cart_user, "num_carts_total": num_carts_total}

    return render(request, "cart.html", context=context)


def cart_item_detail(request, cart_pk, item_pk):
    cart_item = get_object_or_404(CartItem, pk=item_pk, cart_id=cart_pk)

    product = cart_item.product
    quantity = cart_item.quantity

    context = {"product": product, "quantity": quantity}

    return render(request, "cart_item_detail.html", context=context)
