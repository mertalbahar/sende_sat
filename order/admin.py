from django.contrib import admin

from .models import Cart


@admin.register(Cart)
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'product', 'quantity', 'price', 'subtotal')
    list_filter = ['user']