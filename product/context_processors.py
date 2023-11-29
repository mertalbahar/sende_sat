from .models import Category, Product


def category(request):
    return {'categories': Category.objects.all()}


def latest_products(request):
    return {'latest_products': Product.objects.order_by('-id')[:6]}


def featured_products(request):
    return {'featured_products': Product.objects.order_by('?')[:16]}