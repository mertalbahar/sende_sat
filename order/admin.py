from django.contrib import admin

from .models import Cart, Order, OrderProduct


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ( 'user_tag', 'product_tag', 'quantity', 'price', 'subtotal')
    list_filter = ['user']


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'subtotal')
    can_delete = False
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'city', 'total', 'status')
    list_filter = ['status']
    readonly_fields = ('user_tag', 'address', 'city', 'country', 'phone', 'first_name', 'last_name', 'ip', 'total')
    can_delete = False
    inlines = [OrderProductInline]
    

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('user_tag', 'product_tag', 'price', 'quantity', 'subtotal')
    list_filter = ['user']