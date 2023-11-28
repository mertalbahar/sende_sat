from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
]