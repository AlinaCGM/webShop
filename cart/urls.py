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
]
