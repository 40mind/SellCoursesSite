from django.shortcuts import render
from .models import Direction, Course, Person
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class AdminCourseDetailView(generic.DetailView):
    model = Course
    template_name = "admin_course_detail.html"

class AdminPersonDetailView(generic.DetailView):
    model = Person
    template_name = "admin_person_detail.html"

class PersonCreate(CreateView):
    model = Person
    fields = ['course', 'name', 'surname', 'fathername', 'email', 'phone', 'comment']
    template_name = "person_form.html"
    success_url = '/courses/'

class AdminDirectionCreate(CreateView):
    model = Direction
    fields = ['name']
    template_name = "direction_form_admin.html"
    success_url = '/courses/admin/directions/'

class AdminDirectionUpdate(UpdateView):
    model = Direction
    fields = ['name']
    template_name = "direction_form_admin.html"
    success_url = '/courses/admin/directions/'

class AdminDirectionDelete(DeleteView):
    model = Direction
    template_name = 'direction_confirm_delete.html'
    success_url = '/courses/admin/directions/'

class AdminCourseCreate(CreateView):
    model = Course
    fields = '__all__'
    template_name = "course_form_admin.html"
    success_url = '/courses/admin/courses/'

class AdminCourseUpdate(UpdateView):
    model = Course
    fields = '__all__'
    template_name = "course_form_admin.html"
    success_url = '/courses/admin/courses/'

class AdminCourseDelete(DeleteView):
    model = Course
    template_name = 'course_confirm_delete.html'
    success_url = '/courses/admin/courses/'

class AdminPersonCreate(CreateView):
    model = Person
    fields = '__all__'
    template_name = "person_form_admin.html"
    success_url = '/courses/admin/people/'

class AdminPersonUpdate(UpdateView):
    model = Person
    fields = '__all__'
    template_name = "person_form_admin.html"
    success_url = '/courses/admin/people/'

class AdminPersonDelete(DeleteView):
    model = Person
    template_name = 'person_confirm_delete.html'
    success_url = '/courses/admin/people/'
