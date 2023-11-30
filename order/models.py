from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.product.title
    
    @property
    def price(self):
        return self.product.price
    
    @property
    def subtotal(self):
        return self.quantity * self.product.price