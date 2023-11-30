from order.models import Cart


def cart_total(request):
    cart = Cart.objects.filter(user_id = request.user.id)
    total = 0
    
    for item in cart:
        total += item.product.price * item.quantity
    
    return {'total': total}