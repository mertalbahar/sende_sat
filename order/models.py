from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1, verbose_name='Adet')
    
    class Meta:
        verbose_name = 'Sepet'
        verbose_name_plural = 'Sepetler'
    
    def __str__(self):
        return self.product.title
    
    @property
    def price(self):
        return self.product.price
    
    @property
    def subtotal(self):
        return self.quantity * self.product.price
    
    def user_tag(self):
        return self.user
    
    user_tag.short_description = 'Kullanıcı'
    
    def product_tag(self):
        return self.product
    
    product_tag.short_description = 'Ürün'


class Order(models.Model):
    STATUS = (
        ('Yeni', 'Yeni'),
        ('İşleme Alındı', 'İşleme Alındı'),
        ('Tamamlandı', 'Tamamlandı'),
        ('İptal Edildi', 'İptal Edildi'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5, editable=False)
    first_name = models.CharField(max_length=10, verbose_name='İsim')
    last_name = models.CharField(max_length=10, verbose_name='Soyisim')
    phone = models.CharField(max_length=20, verbose_name='Tel')
    address = models.CharField(max_length=150, verbose_name='Adres')
    city = models.CharField(max_length=20, verbose_name='Şehir')
    country = models.CharField(max_length=20, verbose_name='Ülke')
    total = models.FloatField(verbose_name='Tutar')
    status=models.CharField(max_length=15, choices=STATUS, default='Yeni', verbose_name='Durum')
    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100, verbose_name='Not')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')
    updated_at=models.DateTimeField(auto_now=True, verbose_name='Güncellenme')
    
    class Meta:
        verbose_name = 'Sipariş'
        verbose_name_plural = 'Siparişler'

    def __str__(self):
        return self.code
    
    def user_tag(self):
        return self.user
    
    user_tag.short_description = 'Kullanıcı'
    

class OrderProduct(models.Model):
    STATUS = (
        ('Yeni', 'Yeni'),
        ('İşleme Alındı', 'İşleme Alındı'),
        ('Hazırlanıyor', 'Hazırlanıyor'),
        ('Kargolandı', 'Kargolandı'),
        ('Tamamlandı', 'Tamamlandı'),
        ('İptal Edildi', 'İptal Edildi'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Adet')
    price = models.FloatField(verbose_name='Fiyat')
    subtotal = models.FloatField(verbose_name='Toplam')
    status = models.CharField(max_length=15, choices=STATUS, default='Yeni', verbose_name='Durum')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme')
    
    class Meta:
        verbose_name = 'Sipariş Ürün'
        verbose_name_plural = 'Sipariş Ürünler'

    def __str__(self):
        return self.product.title
    
    def user_tag(self):
        return self.user
    
    user_tag.short_description = 'Kullanıcı'
    
    def product_tag(self):
        return self.product
    
    product_tag.short_description = 'Ürün'