from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product'),
    path('<slug:c_slug>', views.category_products, name='category_products'),
    path('<slug:c_slug>/<slug:p_slug>', views.product_detail, name='product_detail'),
]