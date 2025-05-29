from django.contrib import admin
from .models import EducationalProgram

@admin.register(EducationalProgram)
class EducationalProgramAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'name', 'grade', 'date_added']
    list_filter = ['grade', 'date_added']
    search_fields = ['student_name', 'name']
    ordering = ['-date_added']
