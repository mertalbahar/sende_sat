from .models import SiteSetting


def setting(request):
    setting = SiteSetting.objects.get(pk=1)
    
    if setting:
        return {'setting': setting}
    
    
def page(request):
    page = request.get_full_path()
    pages = {
        '/': 'anasayfa',
        '/product/': 'ürünler',
        '/user/': 'kullanıcı Profili',
        '/user/login': 'kullanıcı Girişi',
        '/user/register': 'kullanıcı Kayıt',
        '/user/update': 'profil Güncelleme',
    }
    
    print(f'Page Length: {len(page)}, Page List: {page}')
    
    if page == '/':
        return {'page': pages[page]}
    
    else: 
        if page in pages:
            return {'page': pages[page]}
        else:
            page = page.split('/')
            page = [i for i in page if i]
        
            print(f'Page Length: {len(page)}, Page List: {page}')
            
            return {'page': page[1]}