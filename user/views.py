from django.db import transaction
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email

from .models import UserProfile
from .forms import UserLoginForm, UserPasswordChangeForm, UserProfileForm, UserRegisterForm, UserUpdateForm


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    user = User.objects.get(id = request.user.id)
    profile = UserProfile.objects.get(user_id = request.user.id)
    
    context = {
        'user': user,
        'profile': profile
    }
    
    return render(request, 'user/index.html', context)


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


@login_required(login_url=settings.LOGIN_URL)
@transaction.atomic
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance = request.user)
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance = request.user.userprofile)
        
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save( )
            user_profile_form.save()
            messages.add_message(request, messages.SUCCESS, 'Profiliniz güncellendi.')
            
            return redirect('user_profile')
        
    else:
        user_form = UserUpdateForm(instance = request.user)
        user_profile_form = UserProfileForm(instance = request.user.userprofile)
        
    context = {
        'user_form': user_form,
        'user_profile_form': user_profile_form
    }
    
    return render(request, 'user/update.html', context)


@login_required(login_url=settings.LOGIN_URL)
def user_password_change(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, 'Parola güncellendi.')
            
            return redirect('user_profile')
        
        else:
            return render(request, 'user/password_change.html', {'form': form})
        
    else:
        form = UserPasswordChangeForm(request.user)
        
        return render(request, 'user/password_change.html', {'form': form})