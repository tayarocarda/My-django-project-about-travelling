from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Category, Page

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order', 'description_preview')
    list_editable = ('order',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order', 'name')
    
    def description_preview(self, obj):
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    description_preview.short_description = 'Описание'

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'order', 'created', 'modified', 'image_preview')
    list_filter = ('is_published', 'category', 'created', 'modified')
    list_editable = ('is_published', 'order', 'category')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created', 'modified', 'image_preview')
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'category', 'featured_image', 'image_preview')
        }),
        ('Содержание', {
            'fields': ('content', 'excerpt')
        }),
        ('Настройки публикации', {
            'fields': ('is_published', 'order', 'created', 'modified')
        }),
        ('META данные', {
            'fields': ('meta_keywords', 'meta_description'),
            'classes': ('collapse',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.featured_image.url)
        return "Нет изображения"
    image_preview.short_description = 'Превью изображения'
