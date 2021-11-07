from django.db import models
from django.urls import reverse
# Create your models here.

class Direction(models.Model):
    name = models.CharField(max_length=30, help_text="Название направления")

    def __str__(self):
        return self.name

    def get_absolute_url_update(self):
        return reverse('admin_direction_update', args=[str(self.id)])

    def get_absolute_url_delete(self):
        return reverse('admin_direction_delete', args=[str(self.id)])

class Course(models.Model):
    name = models.CharField(max_length=30, help_text="Название курса")
    num = models.IntegerField(help_text="Количество занятий")
    time = models.IntegerField(help_text="Время одного занятия")
    days = models.CharField(max_length=100, help_text="Дни недели когда будут проходить занятия (через запятую)")
    firstdate = models.DateField(help_text="Дата первого занятия")
    lastdate = models.DateField(help_text="Дата последнего занятия")
    price = models.IntegerField(help_text="Стоимость курса")
    info = models.TextField(help_text="Подробная информацая про курс")
    direction = models.ForeignKey("Direction", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])

    def get_absolute_url_admin(self):
        return reverse('admin_course_detail', args=[str(self.id)])

    def get_absolute_url_update(self):
        return reverse('admin_course_update', args=[str(self.id)])

    def get_absolute_url_delete(self):
        return reverse('admin_course_delete', args=[str(self.id)])

class Person(models.Model):
    course = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20, help_text="Имя")
    surname = models.CharField(max_length=30, help_text="Фамилия")
    fathername = models.CharField(max_length=30, help_text="Отчество")
    email = models.EmailField(help_text="Электронная почта")
    phone = models.CharField(max_length=12, help_text="Номер телефона")
    comment = models.TextField(null=True, help_text="Комментарий", blank=True)
    pay = models.BooleanField(default=False, help_text="Есть ли оплата")
    dateofpay = models.DateField(null=True, help_text="Дата оплаты", blank=True)

    def __str__(self):
        return self.surname

    def get_absolute_url_admin(self):
        return reverse('admin_person_detail', args=[str(self.id)])

    def get_absolute_url_update(self):
        return reverse('admin_person_update', args=[str(self.id)])

    def get_absolute_url_delete(self):
        return reverse('admin_person_delete', args=[str(self.id)])