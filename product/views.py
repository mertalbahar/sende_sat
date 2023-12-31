from django.db.models import Count
from django.conf import settings
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from user.models import FavoriteProduct

from .forms import CommentForm
from .models import Category, Comment, Product, ProductDiscount, ProductImages


def index(request):
    products = Product.objects.filter(status = True)
    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)
    active_products = products.count()
    
    context = {
        'page_obj': page_obj,
        'active_products': active_products
    }

    return render(request, 'product/index.html', context)


def product_detail(request, c_slug, p_slug):
    product = Product.objects.get(slug = p_slug)
    images = ProductImages.objects.filter(product = product)
    related_products = Product.objects.filter(category = product.category).exclude(slug = product.slug).exclude(status = False)
    comments = Comment.objects.filter(product = product, status = 'Onaylandı')
    ratings = comments.values('rate').annotate(Count('rate'))
    favorites = FavoriteProduct.objects.filter(user_id = request.user.id, product = product)
    discount = ProductDiscount.objects.filter(product = product)
    
    if discount:
        discount = discount.get(product = product)
        
    
    context = {
        'product': product,
        'images': images,
        'related_products': related_products,
        'comments': comments,
        'ratings': ratings,
        'favorites': favorites,
        'discount': discount
    }
    
    return render(request, 'product/product_detail.html', context)


def category_products(request, c_slug):
    category = Category.objects.get(slug = c_slug)
    products = list(Product.objects.filter(category = category, status = True))
    active_products = Product.objects.filter(category = category, status = True).count()
    
    node = category
    children = Category.objects.add_related_count(node.get_children(), Product, 'category', 'product_counts')
    
    for i in children:
        a = list(Product.objects.filter(category__slug = i.slug, status = True))
        products.extend(a)
        
    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)
    
    context = {
        'page_obj': page_obj,
        'active_products': active_products
    }
    
    return render(request, 'product/index.html', context)


def discount_products(request):
    products = ProductDiscount.objects.all().order_by('-discount')
    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)
    active_products = products.count()
    
    context = {
        'page_obj': page_obj,
        'active_products': active_products
    }
    
    return render(request, 'product/special_offer.html', context)


def search(request):
    url = request.META.get('HTTP_REFERER')
    if 'query' in request.GET and request.GET['query'] != '':
        query = request.GET['query']
        category = request.GET.get('category', None)
        
        if category != 'Kategoriler':
            products = Product.objects.filter(status = True, category__title = category, title__icontains = query)
            
        else:
            products = Product.objects.filter(status = True, title__icontains = query)
            
        paginator = Paginator(products, 6)
        page = request.GET.get('page', 1)
        page_obj = paginator.page(page)
        
    else:
        return redirect(url)
    
    context = {
        'page_obj': page_obj,
        'query': query
    }
    
    return render(request, 'product/index.html', context)


@login_required(login_url=settings.LOGIN_URL)
def add_comment(request, id):
    url = request.META.get('HTTP_REFERER')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            data = Comment()
            data.product_id = id
            data.user_id = request.user.id
            data.ip = request.META.get('REMOTE_ADDR')
            data.rate = form.cleaned_data['rate']
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.save()
            messages.success(request, "Yorumunuz gönderilmiştir, teşekkür ederiz.")
            
            return redirect(url)
    
    return redirect(url)