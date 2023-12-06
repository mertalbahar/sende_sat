from django.contrib import admin

from .models import ContactMessage, SiteSetting


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'updated_at', 'status')
    readonly_fields =('name', 'subject', 'email', 'message', 'ip')
    list_filter = ['status']