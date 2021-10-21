from django.db import models
from django.urls import reverse

# Create your models here.
class Direction(models.Model):
    name = models.CharField(max_length=30, help_text="Введите название направления")

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=30, help_text="Введите название курса")
    num = models.IntegerField(help_text="Введите количество занятий")
    time = models.IntegerField(help_text="Введите время одного занятия")
    days = models.CharField(max_length=100, help_text="Введите дни недели когда будут проходить занятия (через запятую)")
    firstdate = models.DateField(help_text="Введите дату первого занятия")
    lastdate = models.DateField(help_text="Введите дату последнего занятия")
    price = models.IntegerField(help_text="Введите стоимость курса")
    info = models.TextField(help_text="Введите подробную информацию про курс")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course-detail', args=[str(self.name)])

