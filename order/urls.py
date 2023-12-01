from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='order'),
    path('cart', views.cart, name='cart'),
    path('add_cart/<int:id>', views.add_cart, name='add_cart'),
    path('remove_cart/<int:id>', views.remove_cart, name='remove_cart'),
]