from django.urls import path
from . import views
from cart.views import CartDetailView

urlpatterns = [
    # Define your URL patterns here
<<<<<<< HEAD
    path("<int:pk>/", views.cart, name="cart"),
    path(
        "<int:cart_pk>/item/<uuid:item_pk>/",
        views.cart_item_detail,
        name="cartitem-detail",
    ),
=======
    # For example:
    # path('cart/', views.cart_view, name='cart'),
    # path("<int:pk>", views.cart_view, name="cart-detail"),
>>>>>>> c114fd4df0ea3f98c0f7840d03d9edc7ff94b5af
]