from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from product.models import Product

from .models import Cart
from .forms import CartForm


def index(request):
    return render(request, 'order/index.html')


def cart(request):
    cart = Cart.objects.filter(user_id = request.user.id)
        
    context = {
        'cart': cart,
    }
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(username)
        print(password)
        
        user = authenticate(request, username = username, password = password)
            
        if user is not None:
            login(request, user)
            
            return redirect(request.META.get('HTTP_REFERER'))
        
        else:
            return render(request, 'order/cart.html', {'error': 'Kullanıcı adı ya da parola hatalı.'})
        
    else:
        return render(request, 'order/cart.html', context)


@login_required(login_url=settings.LOGIN_URL)
def add_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id = id)
    cart_product = Cart.objects.filter(product = product, user_id = request.user.id)
    
    if request.method == 'POST':
        form = CartForm(request.POST)
        
        if form.is_valid():
            if cart_product.exists():
                data = Cart.objects.get(product_id = id, user_id = request.user.id)
                data.quantity += form.cleaned_data.get('quantity')
                data.save()
                
            else:
                data = Cart()
                data.user_id = request.user.id
                data.product_id = id
                data.quantity =form.cleaned_data.get('quantity')
                data.save()
                
        messages.success(request, 'Ürün sepete eklendi.')
        request.session['cart_items'] = Cart.objects.filter(user_id = request.user.id).count()
        
        return redirect(url)
    
    else:
        if cart_product.exists():
            data = Cart.objects.get(product_id = id, user_id = request.user.id)
            data.quantity += 1
            data.save()
            
        else:
            data = Cart()
            data.user_id = request.user.id
            data.product_id = id
            data.quantity = 1
            data.save()
    
    messages.success(request, 'Ürün sepete eklendi.')
    request.session['cart_items'] = Cart.objects.filter(user_id = request.user.id).count()
    return redirect(url)