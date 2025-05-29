from django.shortcuts import render, redirect
from .models import EducationalProgram
from .forms import ProgramForm, ProgramFilterForm
from django.db.models import Avg, Sum, Q

def index(request):
    return render(request, 'app1/index.html')

def program_list(request):
    # Получаем все программы
    programs = EducationalProgram.objects.all()
    
    # Создаем форму фильтрации
    filter_form = ProgramFilterForm(request.GET)
    
    if filter_form.is_valid():
        # Применяем поиск
        search = filter_form.cleaned_data.get('search')
        if search:
            programs = programs.filter(
                Q(student_name__icontains=search) | 
                Q(name__icontains=search)
            )
        
        # Применяем фильтр по оценкам
        min_grade = filter_form.cleaned_data.get('min_grade')
        if min_grade is not None:
            programs = programs.filter(grade__gte=min_grade)
            
        max_grade = filter_form.cleaned_data.get('max_grade')
        if max_grade is not None:
            programs = programs.filter(grade__lte=max_grade)
        
        # Применяем сортировку
        sort_by = filter_form.cleaned_data.get('sort_by')
        if sort_by:
            programs = programs.order_by(sort_by)
        else:
            programs = programs.order_by('-date_added')  # По умолчанию сортируем по дате
    
    # Вычисляем статистику
    avg_grade = programs.aggregate(Avg('grade'))['grade__avg']
    total = programs.count()
    
    return render(request, 'app1/list.html', {
        'programs': programs,
        'avg_grade': avg_grade,
        'total': total,
        'filter_form': filter_form
    })

def add_program(request):
    if request.method == "POST":
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm()
    return render(request, 'app1/form.html', {'form': form})
