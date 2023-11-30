from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Cart, CartItem
from product.models import Product


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

    return render(
        request, "product/product_list.html", context={"cart_item": cart_item}
    )


def cart_item_detail(request, cart_pk, item_pk):
    product = cart_item.product
    quantity = cart_item.quantity

    context = {"product": product, "quantity": quantity}

    return render(request, "cart_item_detail.html", context=context)
