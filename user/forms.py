from django import forms
from django.forms import widgets
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from .models import UserProfile


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        
        
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class': 'form-control'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        
        self.fields['email'].required = True
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email = email).exists():
            self.add_error('email', 'Email daha önce kullanılmış.')
            
        return email
    
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        
        
CITY = (
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
)
        
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['address'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['city'].widget = widgets.Select(choices=CITY, attrs={'class': 'form-control'})
        self.fields['country'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['image'].widget = widgets.FileInput(attrs={'class': 'form-control'})
        
        
class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})