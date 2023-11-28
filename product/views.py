from django.shortcuts import render

from .models import Product, ProductImages


def index(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {'products': products})


def product_detail(request, slug):
    product = Product.objects.get(slug = slug)
    images = ProductImages.objects.filter(product = product)
    related_products = Product.objects.filter(category = product.category).exclude(slug = product.slug)
    
    context = {
        'product': product,
        'images': images,
        'related_products': related_products
    }
    
    return render(request, 'product/product_detail.html', context)