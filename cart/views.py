from django.shortcuts import render

# Create your views here.

from django.views.generic import DetailView
from .models import Cart, CartItem
from django.shortcuts import get_object_or_404


class CartDetailView(DetailView):
    model = Cart
    template_name = "cart.html"


# TODO Use the built in UpdateView for quantity form
# plus DeleteView for remove button


def cart_item_detail(request, cart_pk, item_pk):
    cart_item = get_object_or_404(CartItem, pk=item_pk, cart_id=cart_pk)

    product = cart_item.product
    quantity = cart_item.quantity

    context = {"product": product, "quantity": quantity}

    return render(request, "cart_item_detail.html", context=context)
