from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='order'),
    path('order', views.order_product, name='order_product'),
    path('cart', views.cart, name='cart'),
    path('order_detail/<int:id>', views.order_detail, name='order_detail'),
    path('add_cart/<int:id>', views.add_cart, name='add_cart'),
    path('remove_cart/<int:id>', views.remove_cart, name='remove_cart'),
]