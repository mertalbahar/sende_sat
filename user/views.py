from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.validators import validate_email

from .forms import UserLoginForm, UserRegisterForm


def index(request):
    return render(request, 'user/index.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Başarılı bir şekilde oturum açtınız.')
                next_url = request.GET.get('next', None)
                
                if next_url is None:
                    return redirect('/')
                else:
                    return redirect(next_url)
                
            else:
                return render(request, 'user/login.html', {'form': form})
            
        else:
            return render(request, 'user/login.html', {'form': form})
        
    else:
        form = UserLoginForm()
        return render(request, 'user/login.html', {'form': form})
    

def user_logout(request):
    messages.add_message(request, messages.SUCCESS, 'Başarılı bir şekilde çıkış yaptınız.')
    logout(request)
    
    return redirect('/')


def user_register(request):
    if 'emailcheck' in request.POST:
        email = request.POST.get('emailcheck')
    
        try:
            validate_email(email)
            
            if User.objects.filter(email = email).exists():
                messages.add_message(request, messages.ERROR, 'Email daha önce kullanılmış.')
                return redirect('user_login')
                
        except:
            messages.add_message(request, messages.ERROR, 'Lütfen geçerli bir email giriniz.')
            return redirect('user_login')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Başarılı şekilde kayıt oldunuz.')
            
            return redirect('/')
        
        else:
            return render(request, 'user/register.html', {'form': form})
    
    else:
        form = UserRegisterForm()
        return render(request, 'user/register.html', {'form': form})