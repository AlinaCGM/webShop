from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here

    path("<int:pk>/", views.cart, name="cart"),
    path(
        "<int:cart_pk>/item/<uuid:item_pk>/",
        views.cart_item_detail,
        name="cartitem-detail",
    ),

    # For example:
    # path('cart/', views.cart_view, name='cart'),
    # path("<int:pk>", views.cart_view, name="cart-detail"),

]
