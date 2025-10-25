from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Shoe, Type, Color, Material, ShoeImage


class ShoeImageInline(admin.TabularInline):
    model = ShoeImage
    extra = 1
    readonly_fields = ['image_preview']  # відображаємо мініатюру
    fields = ['image', 'image_preview']  # порядок полів

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" height="150" style="object-fit:contain;"/>')
        return "-"

    image_preview.short_description = "Превʼю зображення"


@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    inlines = [ShoeImageInline]
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    fieldsets = (
        ('Основна інформація', {
            'fields': ['name', 'price', ('image', 'image_preview'), 'type', 'color', 'season', 'material', 'size_from', 'size_to']
        }),
        ('Статуси', {
            'fields': ['is_bestseller', 'is_new_shoes', 'is_active']
        }),
        ('Час створення/оновлення', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse',],
        }),
    )
    list_display = ['name', 'image_preview', 'type',  'price', 'is_active', 'is_bestseller', 'is_new_shoes']
    search_fields = ['name']
    list_filter = ['type', 'season', 'material', 'is_active', 'color']
    list_editable = ['is_bestseller', 'is_new_shoes', 'is_active']
    ordering = ["-updated_at"]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="150" style="object-fit:contain;" />', obj.image.url)
        return "-"

    image_preview.short_description = 'Фото'
    image_preview.admin_order_field = 'image'


admin.site.register(Type)
admin.site.register(Color)
admin.site.register(Material)