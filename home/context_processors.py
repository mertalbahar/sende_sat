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
        '/user/': 'kullanıcı profili',
        '/user/login': 'kullanıcı girişi',
        '/user/register': 'kullanıcı kayıt',
        '/user/update': 'profil güncelleme',
        '/user/password': 'şifre güncelleme',
        '/order/': 'siparişler',
        '/order/cart': 'sepet',
    }
    
    if page in pages:
        return {'page': pages[page]}
    else:
        page = page.split('/')
        page = [i for i in page if i]
    
        if len(page) == 1:
            return {'page': page[0]}
        else:
            return {'page': page[1]}