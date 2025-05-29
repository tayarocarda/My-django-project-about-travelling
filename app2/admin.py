from django.contrib import admin
from django.utils.html import format_html
from .models import Page, ContentCard, AcademicSupervisor, ProgramManager, Classmate

class ContentCardInline(admin.TabularInline):
    model = ContentCard
    extra = 1
    fields = ('title', 'description', 'icon', 'order', 'is_active')

class ProgramManagerInline(admin.TabularInline):
    model = ProgramManager
    extra = 1
    fields = ('name', 'photo', 'email', 'responsibilities', 'order')

class ClassmateInline(admin.TabularInline):
    model = Classmate
    extra = 1
    fields = ('name', 'photo', 'email', 'phone', 'interests', 'order')

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'slug', 'content', 'is_published', 'meta_description')
        }),
        ('Страница "Я"', {
            'fields': ('full_name', 'photo', 'email', 'phone', 'resume'),
            'classes': ('collapse',)
        }),
        ('Страница "Моя программа"', {
            'fields': ('program_name', 'program_link', 'skills', 'advantages', 'prospects'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [ContentCardInline]
    
    def get_inlines(self, request, obj):
        if obj and obj.slug == 'program-management':
            return [ContentCardInline, ProgramManagerInline]
        elif obj and obj.slug == 'my-classmates':
            return [ContentCardInline, ClassmateInline]
        return [ContentCardInline]

@admin.register(AcademicSupervisor)
class AcademicSupervisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'page')
    search_fields = ('name', 'email')

@admin.register(ContentCard)
class ContentCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'order', 'is_active')
    list_filter = ('page', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('order', 'is_active')