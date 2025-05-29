from django.db import models
from django.urls import reverse

class Page(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Содержание")
    slug = models.SlugField("URL", unique=True)
    is_published = models.BooleanField("Опубликовано", default=True)
    meta_description = models.CharField("Meta описание", max_length=160, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Поля для страницы "Я"
    full_name = models.CharField("ФИО", max_length=255, blank=True)
    photo = models.ImageField("Фото", upload_to='profile/', blank=True, null=True)
    email = models.EmailField("Email", blank=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    resume = models.FileField("Резюме", upload_to='resumes/', blank=True, null=True)

    # Поля для страницы "Моя программа"
    program_name = models.CharField("Название программы", max_length=255, blank=True)
    program_link = models.URLField("Ссылка на программу", blank=True)
    skills = models.TextField("Чему научусь", blank=True)
    advantages = models.TextField("Преимущества программы", blank=True)
    prospects = models.TextField("Перспективы после обучения", blank=True)

    def __str__(self):
        return self.title

class ContentCard(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание')
    icon = models.CharField('Иконка', max_length=50, 
                          help_text='Название иконки из Material Icons')
    slug = models.SlugField('URL', unique=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, 
                           related_name='cards', null=True, blank=True)
    order = models.IntegerField('Порядок отображения', default=0)
    is_active = models.BooleanField('Активно', default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class AcademicSupervisor(models.Model):
    page = models.OneToOneField(Page, on_delete=models.CASCADE, 
                              related_name='supervisor', 
                              limit_choices_to={'slug': 'program-management'})
    name = models.CharField("ФИО", max_length=255)
    photo = models.ImageField("Фото", upload_to='supervisors/', blank=True, null=True)
    email = models.EmailField("Email")
    bio = models.TextField("Биография", blank=True)

    def __str__(self):
        return self.name

class ProgramManager(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, 
                           related_name='managers',
                           limit_choices_to={'slug': 'program-management'})
    name = models.CharField("ФИО", max_length=255)
    photo = models.ImageField("Фото", upload_to='managers/', blank=True, null=True)
    email = models.EmailField("Email")
    responsibilities = models.TextField("Обязанности", blank=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Classmate(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, 
                           related_name='classmates',
                           limit_choices_to={'slug': 'my-classmates'})
    name = models.CharField("ФИО", max_length=255)
    photo = models.ImageField("Фото", upload_to='classmates/', blank=True, null=True)
    email = models.EmailField("Email", blank=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    interests = models.TextField("Интересы", blank=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name