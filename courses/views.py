from django.shortcuts import render
from .models import Direction, Course, Person
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

@login_required
def admin(request):
    return render(
        request,
        "admin.html",
    )

@login_required
def admin_directions(request):
    obj_dir = Direction.objects.all()

    return render(
        request,
        "admin_directions.html",
        context={'direction_list': obj_dir},
    )

@login_required
def admin_courses(request):
    obj_cour = Course.objects.all()

    return render(
        request,
        "admin_courses.html",
        context={'course_list': obj_cour},
    )

@login_required
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

class AdminCourseDetailView(LoginRequiredMixin, generic.DetailView):
    model = Course
    template_name = "admin_course_detail.html"

class AdminPersonDetailView(LoginRequiredMixin, generic.DetailView):
    model = Person
    template_name = "admin_person_detail.html"

class PersonCreate(CreateView):
    model = Person
    fields = ['course', 'name', 'surname', 'fathername', 'email', 'phone', 'comment']
    template_name = "person_form.html"
    success_url = '/courses/'

class AdminDirectionCreate(LoginRequiredMixin, CreateView):
    model = Direction
    fields = ['name']
    template_name = "direction_form_admin.html"
    success_url = '/courses/admin/directions/'

class AdminDirectionUpdate(LoginRequiredMixin, UpdateView):
    model = Direction
    fields = ['name']
    template_name = "direction_form_admin.html"
    success_url = '/courses/admin/directions/'

class AdminDirectionDelete(LoginRequiredMixin, DeleteView):
    model = Direction
    template_name = 'direction_confirm_delete.html'
    success_url = '/courses/admin/directions/'

class AdminCourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    fields = '__all__'
    template_name = "course_form_admin.html"
    success_url = '/courses/admin/courses/'

class AdminCourseUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    fields = '__all__'
    template_name = "course_form_admin.html"
    success_url = '/courses/admin/courses/'

class AdminCourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'course_confirm_delete.html'
    success_url = '/courses/admin/courses/'

class AdminPersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = '__all__'
    template_name = "person_form_admin.html"
    success_url = '/courses/admin/people/'


class AdminPersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = '__all__'
    template_name = "person_form_admin.html"
    success_url = '/courses/admin/people/'


class AdminPersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    template_name = 'person_confirm_delete.html'
    success_url = '/courses/admin/people/'
