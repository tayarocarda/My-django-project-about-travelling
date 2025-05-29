# forms.py

from django import forms
from .models import Page

class PageFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        label='Поиск',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Поиск по содержимому'
        })
    )

    SORT_CHOICES = [
        ('name', 'По имени (А-Я)'),
        ('-name', 'По имени (Я-А)'),
        ('email', 'По email'),
        ('created', 'По дате'),
    ]
    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        initial='name',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'aria-label': 'Сортировка'
        })
    )
    is_published = forms.ChoiceField(
        choices=[
            ('', 'Все страницы'),
            ('1', 'Только опубликованные'),
            ('0', 'Только черновики'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )