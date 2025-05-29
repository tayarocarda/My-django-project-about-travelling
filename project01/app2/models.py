from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("URL", unique=True)
    description = models.TextField("Описание", blank=True)
    order = models.IntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Page(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    slug = models.SlugField("URL", unique=True)
    content = models.TextField("Содержание")
    excerpt = models.TextField("Краткое описание", blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    modified = models.DateTimeField("Дата изменения", auto_now=True)
    is_published = models.BooleanField("Опубликовано", default=True)
    order = models.IntegerField("Порядок", default=0)
    meta_keywords = models.CharField("Meta Keywords", max_length=255, blank=True)
    meta_description = models.CharField("Meta Description", max_length=255, blank=True)
    featured_image = models.ImageField("Изображение", upload_to='pages/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.excerpt and self.content:
            self.excerpt = self.content[:200]
        super().save(*args, **kwargs)