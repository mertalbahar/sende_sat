from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20, verbose_name='Telefon')
    address = models.CharField(blank=True, max_length=150, verbose_name='Adres')
    city = models.CharField(blank=True, max_length=20, verbose_name='Şehir')
    country = models.CharField(blank=True, max_length=50, verbose_name='Ülke')
    image = models.ImageField(blank=True, upload_to='images/users/', verbose_name='Resim')
    
    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    
    image_tag.short_description = 'Resim'
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)