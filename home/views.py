from django.shortcuts import redirect, render
from django.contrib import messages

from .models import ContactMessage
from .forms import ContactMessageForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız gönderilmiştir. Teşekkür ederiz.")
            
            return redirect('contact')
        
        else:
            return render(request, 'contact.html', {'form': form})
        
    form = ContactMessageForm()
    
    return render(request, 'contact.html', {'form': form})