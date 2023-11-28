from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    title = models.CharField(max_length=30, verbose_name='Kategori')
    keywords = models.CharField(max_length=250)
    description = models.TextField(verbose_name='Açıklama')
    image = models.ImageField(blank=True, upload_to='images/category/', verbose_name='Resim')
    status = models.CharField(max_length=10, choices=STATUS, default=False, verbose_name='Yayınla')
    slug = models.SlugField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme')
    
    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
        
    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']
    
    def get_ablosute_url(self):
        return reverse('category_products', kwargs={'slug': self.slug})
    
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        
        while k is not None:
            full_path.append(k.title)
            k = k.parent
            
        return '/'.join(full_path[::-1])
    

class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Ürün')
    keywords = models.CharField(max_length=250)
    description = models.TextField(verbose_name='Açıklama')
    image = models.ImageField(blank=True, upload_to='images/product/', verbose_name='Resim')
    price = models.FloatField(verbose_name='Birim Fiyat')
    quantity = models.IntegerField(default=0, verbose_name='Adet')
    detail = models.TextField(verbose_name='Detay')
    status = models.CharField(max_length=10, choices=STATUS, verbose_name='Yayınla')
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme')
    
    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'
    
    def __str__(self):
        return self.title
    
    def get_ablosute_url(self):
        return reverse('productsUrl', kwargs={'slug': self.slug})
        
    def category_tag(sef):
        return sef.category
    
    category_tag.short_description = 'Kategori'
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
    
    image_tag.short_description = 'Resim'
    
    
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='Başlık')
    image = models.ImageField(blank=True, upload_to='images/product/')
    
    class Meta:
        verbose_name = 'Resim'
        verbose_name_plural = 'Resimler'

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
    
    image_tag.short_description = 'Resim'