from django.urls import path
from .views import ProductListView
from cart.views import cart_add 

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('product/add-to-cart/<int:product_pk>/', cart_add, name='add-to-cart'), 
]
