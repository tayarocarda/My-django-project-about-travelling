from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def regions(request):
    return render(request, 'myapp/regions.html')

def attractions(request):
    return render(request, 'myapp/attractions.html')

def routes(request):
    return render(request, 'myapp/routes.html')

def tips(request):
    return render(request, 'myapp/tips.html')


def task1(request):
    if request.method == 'POST':
        names = request.POST.get('names', '').split()
        scores = request.POST.get('scores', '').split()
        students = zip(names, scores)
        max_score = 0
        best_student = ''
        for name, score in students:
            total = sum(map(int, score.split('-')))
            if total > max_score:
                max_score = total
                best_student = name
        return render(request, 'myapp/task1.html', {'best_student': best_student})
    return render(request, 'myapp/task1.html')

def task2(request):
    if request.method == 'POST':
        x = float(request.POST.get('x', 0))
        y = float(request.POST.get('y', 1))
        z = 1 / (x * y) if x * y != 0 else 'undefined'
        return render(request, 'myapp/task2.html', {'z': z})
    return render(request, 'myapp/task2.html')


def design_school(request):
    context = {
        'student': {
            'full_name': 'Ляч Анастасия Андреевна',
            'photo': 'images/student.jpg',  
            'email': 'a_lyach@mail.ru',
            'phone': '+7 (977) 881-97-45',
        },
        'program': {
            'name': 'Дизайн и программирование',
            'description': 'Бум разработки приложений, сайтов и сервисов привёл к тому, что рынок нуждается в дизайнерах с широкими компетенциями в сфере цифровых технологий. Более того, дизайнеры и сами всё чаще выступают в роли основателей успешных стартапов. Диджитал-дизайнер должен уметь работать с кодом, знать возможности различных технологий, говорить на одном языке с программистами. Таких специалистов и готовит Школа дизайна НИУ ВШЭ на профиле «Дизайн и программирование». Наши студенты проектируют и реализуют сайты, лендинги и приложения, а также учатся ставить задачи квалифицированным разработчикам.',
            'director': {
                'full_name': 'Мещеряков Арсений Владимирович',
                'photo': 'images/director.jpg',  
                'email': 'mescheryakov@mail.ru',
            },
            'manager': {
                'full_name': 'Харитонов Захар Николаевич',
                'photo': 'images/manager.jpg',  
                'email': 'haritonov@mail.ru',
            },
        },
        'classmates': [
            {
                'full_name': 'Зеленкова Александра',
                'photo': 'images/classmate1.jpg',  
                'email': 'aazelenkova@edu.hse.ru',
                'phone': '+7 (968) 763-41-36',
            },
            {
                'full_name': 'Любивая Дарья',
                'photo': 'images/classmate2.jpg',  
                'email': 'dalyubivaya@edu.hse.ru',
                'phone': '+7 (915) 387-01-47',
            },
        ],
    }
    return render(request, 'myapp/design_school.html', context)
