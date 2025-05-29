from django.db import models

class EducationalProgram(models.Model):
    name = models.CharField("Название программы", max_length=200)
    student_name = models.CharField("Имя студента", max_length=100)
    grade = models.FloatField("Оценка")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.name}"
