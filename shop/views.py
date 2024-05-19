from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(completed=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.save()
    return redirect('cart_detail')

def cart_detail(request):
    order = get_object_or_404(Order, completed=False)
    return render(request, 'shop/cart_detail.html', {'order':order})

def checkout(request):
    order = get_object_or_404(Order, completed=False)
    order.completed = True
    order.save()
    return render(request, 'shop/checkout.html', {'order':order})