from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Category, Product, ProductImages


def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)
    active_products = products.count()
    
    context = {
        'products': products,
        'page_obj': page_obj,
        'active_products': active_products
    }

    return render(request, 'product/index.html', context)


def product_detail(request, c_slug, p_slug):
    product = Product.objects.get(slug = p_slug)
    images = ProductImages.objects.filter(product = product)
    related_products = Product.objects.filter(category = product.category).exclude(slug = product.slug)
    
    context = {
        'product': product,
        'images': images,
        'related_products': related_products
    }
    
    return render(request, 'product/product_detail.html', context)


def category_products(request, c_slug):
    category = Category.objects.get(slug = c_slug)
    products = list(Product.objects.filter(category = category))
    active_products = Product.objects.filter(category = category).count()
    
    node = category
    children = Category.objects.add_related_count(node.get_children(), Product, 'category', 'product_counts')
    
    for i in children:
        a = list(Product.objects.filter(category__slug = i.slug))
        products.extend(a)
        
    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)
    
    context = {
        'products': products,
        'page_obj': page_obj,
        'active_products': active_products
    }
    
    return render(request, 'product/index.html', context)