from django.db import transaction
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from ckeditor_uploader.utils import get_random_string

from product.models import Product
from user.models import UserProfile

from .models import Cart, Order, OrderProduct
from .forms import CartForm, OrderForm


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    orders = Order.objects.filter(user_id = request.user.id).order_by('-id')
    active_orders = orders.exclude(status = 'Tamamlandı').exclude(status = 'İptal Edildi').count()
    
    context = {
        'orders': orders,
        'active_orders': active_orders
    }
    
    return render(request, 'order/index.html', context)


@login_required(login_url=settings.LOGIN_URL)
def order_detail(request, id):
    order = Order.objects.get(user_id = request.user.id, id = id)
    order_items = OrderProduct.objects.filter(order = order)
    active_orders = order_items.exclude(status = 'Tamamlandı').exclude(status = 'İptal Edildi').count()
    
    context = {
        'order': order,
        'order_items': order_items,
        'active_orders': active_orders
    }
    
    return render(request, 'order/order_detail.html', context)


@login_required(login_url=settings.LOGIN_URL)
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


@login_required(login_url=settings.LOGIN_URL)
def remove_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    Cart.objects.filter(id = id).delete()
    messages.success(request, 'Ürün sepetten silindi.')
    request.session['cart_items'] = Cart.objects.filter(user_id = request.user.id).count()
    
    return redirect(url)


@login_required(login_url=settings.LOGIN_URL)
@transaction.atomic
def order_product(request):
    cart = Cart.objects.filter(user_id = request.user.id)
    
    print(cart)
    
    if cart.count() == 0:
        messages.add_message(request, messages.WARNING, 'Devam etmeden önce sepetinize ürün ekleyin.')
        
        return redirect('cart')
    
    total = 0
    
    for item in cart:
        total += item.product.price * item.quantity
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        
        if form.is_valid():
            data = Order()
            data.user_id = request.user.id
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string().upper()
            data.code = ordercode
            data.total = total
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.phone = form.cleaned_data['phone']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            data.save()
            
            for item in cart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = item.product_id
                detail.user_id = request.user.id
                detail.quantity = item.quantity
                detail.price = item.product.price
                detail.subtotal = item.subtotal
                detail.save()
                
                product = Product.objects.get(id = item.product_id)
                product.quantity -= item.quantity
                product.save()
                
            Cart.objects.filter(user_id = request.user.id).delete()
            request.session['cart_items'] = 0
            messages.success(request, "Siparişiniz tamamlanmıştır, Teşekkür Ederiz.")
            
            return render(request, 'order/completed.html', {'ordercode': ordercode})
        
        else:
            messages.warning(request, form.errors)
            return redirect("order_product")
    
    form = OrderForm()
    profile = UserProfile.objects.get(user_id = request.user.id)
    
    context = {
        'cart': cart,
        'form': form,
        'profile': profile,
    }
    
    return render(request, 'order/order_product.html', context)