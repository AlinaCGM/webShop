from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from .models import Cart, CartItem
from product.models import Product
from django.contrib import messages


class CartDetailView(DetailView):
    model = Cart
    template_name = "cart.html"


# TODO Use the built in UpdateView for quantity form
# plus DeleteView for remove button


def cart_add(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    # Get the user_id of the user adding to their cart
    user_id = request.user.pk
    cart = get_object_or_404(Cart, user__pk=user_id)

    # Check if cart_item of this product already exists in the cart
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = CartItem.objects.create(cart=cart, product=product)

    messages.success(request, f"{product.title} successfully added to cart.")

    return redirect("product_list")
