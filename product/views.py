from django.shortcuts import render

from .models import Category, Product, ProductImages


def index(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {'products': products})


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
    
    node = category
    children = Category.objects.add_related_count(node.get_children(), Product, 'category', 'product_counts')
    
    for i in children:
        a = list(Product.objects.filter(category__slug = i.slug))
        products.extend(a)
    
    context = {
        'products': products
    }
    
    return render(request, 'product/index.html', context)