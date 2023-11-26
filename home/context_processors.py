from .models import SiteSetting


def setting(request):
    setting = SiteSetting.objects.get(pk=1)
    
    if setting:
        return {'setting': setting}