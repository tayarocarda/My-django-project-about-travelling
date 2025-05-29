from django import forms
from .models import EducationalProgram

class ProgramForm(forms.ModelForm):
    class Meta:
        model = EducationalProgram
        fields = ['name', 'student_name', 'grade']

class ProgramFilterForm(forms.Form):
    search = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Поиск по имени студента или программе'
        })
    )
    min_grade = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Мин. оценка',
            'step': '0.1'
        })
    )
    max_grade = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Макс. оценка',
            'step': '0.1'
        })
    )
    sort_by = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Сортировка'),
            ('student_name', 'По имени студента'),
            ('name', 'По названию программы'),
            ('grade', 'По оценке (возр.)'),
            ('-grade', 'По оценке (убыв.)'),
            ('date_added', 'По дате добавления (стар.)'),
            ('-date_added', 'По дате добавления (нов.)')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )