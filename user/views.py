from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import UserLoginForm


def index(request):
    return render(request, 'user/index.html')


def user_login(request):
    if request.user.is_authenticated and 'next' in request.GET:
        return render(request, 'user/login.html', {'error': 'Yetkiniz yok.'})
    
    if request.method == 'POST':
        form = UserLoginForm(request, data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Başarılı bir şekilde oturum açtınız.')
                next_url = request.GET.get('next', None)
                
                if next_url is None:
                    return redirect('home')
                else:
                    return redirect(next_url)
                
            else:
                return render(request, 'home', {'form': form})
            
        else:
            return render(request, 'user/login.html', {'form': form})
        
    else:
        form = UserLoginForm()
        return render(request, 'user/login.html', {'form': form})