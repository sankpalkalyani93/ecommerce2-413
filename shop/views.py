from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/login.html', {'form': form})