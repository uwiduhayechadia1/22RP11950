from django.shortcuts import render
from .models import Product

def product_list(request):
    try:
        products = Product.objects.all()
    except Product.DoesNotExist:
        products = []
    return render(request, 'product_list.html', {'products': products})
