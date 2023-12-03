from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView
from .models import Cart, CartItem
from product.models import Product
from django.contrib import messages
from django.urls import reverse_lazy  # Added this import

class CartDetailView(DetailView):
    model = Cart
    template_name = "cart.html"

# Removed the TODO comment as it's not necessary in this code snippet

@login_required
def cart_add(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    user_id = request.user.pk
    cart = get_object_or_404(Cart, user__pk=user_id)

    cart_item = CartItem.objects.filter(cart=cart, product=product).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = CartItem.objects.create(cart=cart, product=product)

    messages.success(request, f"{product.title} successfully added to cart.")

    return redirect("product_list")

class CartItemUpdateView(UpdateView):
    model = CartItem
    fields = ["quantity"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = self.object
        return context

    def get_success_url(self):
        cart_id = self.object.cart.id
        return reverse_lazy("cart", kwargs={"pk": cart_id})  # Used reverse_lazy here
