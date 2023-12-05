from django.forms import ModelForm, TextInput

from .models import Cart, Order


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'phone', 'city', 'country')
        widgets = {
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'İsim'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Soyisim'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'Adres'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': '555 555 55 55'}),
            'city': TextInput(attrs={'class': 'input', 'placeholder': 'Şehir'}),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'Ülke'}),
        }
        labels = {
            'first_name': 'Adınız',
            'last_name': 'Soyadınız',
            'adress': 'Gönderim Adresi',
            'phone': 'İletişim Tel',
            'city': 'Şehir',
            'country': 'Ülke'
        }