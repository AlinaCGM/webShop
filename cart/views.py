from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Cart, CartItem
from django.shortcuts import get_object_or_404


# def cart(request, pk):
#     cart = get_object_or_404(Cart, pk=pk)
#     cart_user = cart.user
#     num_carts_total = Cart.objects.all().count()

#     context = {"cart_user": cart_user, "num_carts_total": num_carts_total}

#     return render(request, "cart.html", context=context)


class CartDetailView(DetailView):
    model = Cart
    template_name = "cart.html"

    """Override get_context_data to get information about CartItems aswell"""

    def get_context_data(self, **kwargs):
        # First call the base/default implementation to get a context
        context = super().get_context_data(**kwargs)
        # Get/Add a QuerySet of all cart items
        context["cart_item_list"] = CartItem.objects.filter(cart=self.object)
        return context


def cart_item_detail(request, cart_pk, item_pk):
    cart_item = get_object_or_404(CartItem, pk=item_pk, cart_id=cart_pk)

    product = cart_item.product
    quantity = cart_item.quantity

    context = {"product": product, "quantity": quantity}

    return render(request, "cart_item_detail.html", context=context)
