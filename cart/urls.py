# from django.urls import path
# from . import views
# from cart.views import CartDetailView, CartItemUpdateView

# urlpatterns = [
#     # Define your URL patterns here
#     path("<int:pk>/", CartDetailView.as_view(), name="cart"),
#     path("<int:pk>/", CartDetailView.as_view(), name="cart"),
#     path(
#         "update/<uuid:pk>/",
#         CartItemUpdateView.as_view(),
#         name="cartitem-update",
#     ),
# ]
from django.urls import path
from .views import CartDetailView, CartItemUpdateView

urlpatterns = [
    path("<int:pk>/", CartDetailView.as_view(), name="cart"),
    path("update/<uuid:pk>/", CartItemUpdateView.as_view(), name="cartitem-update"),
]