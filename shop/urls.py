from django.urls import path
from .views import product_list, login

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('login/', login, name='login')
]
