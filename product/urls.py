from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product'),
    path('search', views.search, name='search'),
    path('special_offer', views.discount_products, name='discount_products'),
    path('add_comment/<int:id>', views.add_comment, name="add_comment"),
    path('<slug:c_slug>', views.category_products, name='category_products'),
    path('<slug:c_slug>/<slug:p_slug>', views.product_detail, name='product_detail'),
]