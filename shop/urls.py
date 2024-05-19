from django.urls import path
from .views import product_list, add_to_cart, cart_detail, checkout

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout')
]
