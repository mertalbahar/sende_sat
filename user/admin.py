from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User

from .models import FavoriteProduct, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name = 'Kullanıcı Profili'
    verbose_name_plural = 'Kullanıcı Profilleri'
    
    
class AccountsUserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(AccountsUserAdmin, self).add_view(*args, **kwargs)
    
    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline]
        return super(AccountsUserAdmin, self).change_view(*args, **kwargs)
    
    
admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)


@admin.register(FavoriteProduct)
class FavoriteProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'user')
    list_filter = ['user']