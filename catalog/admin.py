from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'linked_name')
    search_fields = ('name',)
    ordering = ['name']

    def linked_name(self, obj):
        url = (
            reverse('admin:catalog_product_changelist') +
            f'?category__id__exact={obj.id}'
        )
        return format_html('<a href="{}" style="font-weight:600; color:#007bff;">{}</a>', url, obj.name)

    linked_name.short_description = 'Категория'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_image', 'styled_name', 'colored_price', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    autocomplete_fields = ['category']
    readonly_fields = ['created_at', 'updated_at', 'product_image']
    ordering = ['-created_at']
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category', 'price', 'image')
        }),
        ('Системные данные', {
            'fields': ('created_at', 'updated_at', 'product_image'),
            'classes': ('collapse',),
        }),
    )

    def styled_name(self, obj):
        return format_html('<span style="font-weight:600;">{}</span>', obj.name)
    styled_name.short_description = 'Название'

    def colored_price(self, obj):
        color = "#28a745" if obj.price < 50 else "#dc3545"
        price_formatted = "${:.2f}".format(obj.price)
        return format_html('<span style="color: {};">{}</span>', color, price_formatted)
    colored_price.short_description = 'Цена'

    def product_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px; border-radius:5px;" />', obj.image.url)
        return format_html('<span style="color:#ccc;">Нет изображения</span>')
    product_image.short_description = 'Изображение'

