from django.shortcuts import render

# Create your views here.

from django.views.generic import DetailView
from .models import Cart, CartItem
from django.shortcuts import get_object_or_404


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


# TODO Use the built in UpdateView for quantity form
# plus delete for remove button


def cart_item_detail(request, cart_pk, item_pk):
    cart_item = get_object_or_404(CartItem, pk=item_pk, cart_id=cart_pk)

    product = cart_item.product
    quantity = cart_item.quantity

    context = {"product": product, "quantity": quantity}

    return render(request, "cart_item_detail.html", context=context)
