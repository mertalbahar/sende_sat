from django.forms import ModelForm, TextInput, Textarea

from .models import ContactMessage


class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': TextInput(
                attrs = {
                    'type': 'text',
                    'class': 'form-control input-xlarge',
                    'id': 'name',
                    'placeholder': 'Adınız',
                    'required': 'required',
                    'data-validation-required-message': 'Lütfen Adınızı giriniz'
                }
            ),
            'email': TextInput(
                attrs = {
                    'type': 'email',
                    'class': 'form-control input-xlarge',
                    'id': 'email',
                    'placeholder': 'Email adresiniz',
                    'required': 'required',
                    'data-validation-required-message': 'Lütfen email adresinizi giriniz'
                    }
            ),
            'subject': TextInput(
                attrs = {
                    'type': 'text',
                    'class': 'form-control input-xlarge',
                    'id': 'subject',
                    'placeholder': 'Konu',
                    'required': 'required',
                    'data-validation-required-message': 'Lütfen konuyu giriniz'
                    }
            ),
            'message': Textarea(
                attrs = {
                    'class': 'form-control input-xlarge',
                    'rows': '6',
                    'id': 'message',
                    'placeholder': 'Mesajınız',
                    'required': 'required',
                    'data-validation-required-message': 'Lütfen mesajınızı giriniz'
                }
            ),
        }