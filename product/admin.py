from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from .models import Category, ProductImages, Product


@admin.register(Category)    
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title', 'related_products_count', 'related_products_cumulative_count', 'status')
    list_editable = ('status',)
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Ürün Sayısı (Kategoriye ait)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Ürün Sayısı (Alt kategoriler dahil)'
    
    
class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 5
    readonly_fields = ('image_tag',)
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'category_tag', 'slug', 'status')
    list_editable = ('status',)
    readonly_fields = ('created_at',)
    list_filter = ('status',)
    inlines = [ProductImagesInline]
    list_display_links = ('image_tag', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProductImages)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')