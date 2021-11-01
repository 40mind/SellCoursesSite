from django.shortcuts import render
from .models import Direction, Course, Person
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def home_page(request):
    num_dir = Direction.objects.all().count()
    obj_cour = Course.objects.all()
    obj_dir = Direction.objects.all()

    return render(
        request,
        "home_page.html",
        context={'num_directions': num_dir, 'course_list': obj_cour, 'direction_list': obj_dir},
    )

def admin(request):
    return render(
        request,
        "admin.html",
    )

def admin_directions(request):
    obj_dir = Direction.objects.all()

    return render(
        request,
        "admin_directions.html",
        context={'direction_list': obj_dir},
    )

def admin_courses(request):
    obj_cour = Course.objects.all()

    return render(
        request,
        "admin_courses.html",
        context={'course_list': obj_cour},
    )

def admin_people(request):
    obj_per = Person.objects.all()

    return render(
        request,
        "admin_people.html",
        context={'people_list': obj_per},
    )

class CourseDetailView(generic.DetailView):
    model = Course
    template_name = "course_detail.html"

class PersonCreate(CreateView):
    model = Person
    fields = ['course', 'name', 'surname', 'fathername', 'email', 'phone', 'comment']
    template_name = "person_form.html"

"""
class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
"""