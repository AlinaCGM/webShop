from django.urls import path
from . import views
from cart.views import CartDetailView

urlpatterns = [
    # Define your URL patterns here
    path("<int:pk>/", CartDetailView.as_view(), name="cart"),
    path("add/<int:product_pk>/", views.cart_add, name="add-to-cart"),
]
