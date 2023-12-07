from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user_profile'),
    path('login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('register', views.user_register, name='user_register'),
    path('update', views.user_update, name='user_update'),
    path('password', views.user_password_change, name='user_password_change'),
    path('user_products', views.user_products, name='user_products'),
    path('user_add_product', views.user_add_product, name='user_add_product'),
    path('user_comments', views.user_comments, name='user_comments'),
    path('user_delete_comments/<int:id>', views.user_delete_comments, name='user_delete_comments'),
    path('user_update_product/<slug:slug>', views.user_update_product, name='user_update_product'),
]