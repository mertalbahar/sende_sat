from .models import SiteSetting


def setting(request):
    setting = SiteSetting.objects.get(pk=1)
    
    if setting:
        return {'setting': setting}
    
    
def page(request):
    page = request.get_full_path()
    
    if page == '/':
        return {'page': 'Anasayfa'}
    
    elif page == '/product/':
        return {'page': 'Ürünler'}
    
    else:
        page = page.split('/')
        print(len(page))
        
        if len(page) > 2:
            return {'page': page[len(page)-1]}
        else:
            return {'page': page[1]}