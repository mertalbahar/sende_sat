from django.shortcuts import render

from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {'products': products})