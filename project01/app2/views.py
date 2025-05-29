from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Page

def page_list(request):
    # Получаем параметры фильтрации и сортировки
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'order')
    category_slug = request.GET.get('category', '')
    
    # Базовый QuerySet
    pages = Page.objects.filter(is_published=True)
    categories = Category.objects.all()
    current_category = None
    
    # Фильтрация по категории
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        pages = pages.filter(category=current_category)
    
    # Применяем поиск
    if search_query:
        pages = pages.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(excerpt__icontains=search_query)
        )
    
    # Применяем сортировку
    if sort_by == 'title':
        pages = pages.order_by('title')
    elif sort_by == '-title':
        pages = pages.order_by('-title')
    elif sort_by == 'created':
        pages = pages.order_by('created')
    elif sort_by == '-created':
        pages = pages.order_by('-created')
    elif sort_by == 'modified':
        pages = pages.order_by('modified')
    elif sort_by == '-modified':
        pages = pages.order_by('-modified')
    else:
        pages = pages.order_by('order')
    
    context = {
        'pages': pages,
        'categories': categories,
        'search_query': search_query,
        'sort_by': sort_by,
        'current_category': current_category,
        'user': request.user,
    }
    return render(request, 'app2/page_list.html', context)

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    
    # Получаем другие страницы той же категории
    related_pages = []
    if page.category:
        related_pages = Page.objects.filter(
            category=page.category,
            is_published=True
        ).exclude(id=page.id).order_by('?')[:3]
    
    # Получаем все категории для навигации
    categories = Category.objects.all()
    
    return render(request, 'app2/page_detail.html', {
        'page': page,
        'related_pages': related_pages,
        'categories': categories
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    pages = Page.objects.filter(
        category=category, 
        is_published=True
    ).order_by('order')
    
    # Получаем все категории для навигации
    categories = Category.objects.all()
    
    return render(request, 'app2/category_detail.html', {
        'category': category,
        'pages': pages,
        'categories': categories
    })