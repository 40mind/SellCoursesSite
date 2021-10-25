from django.shortcuts import render
from .models import Direction, Course
from django.views import generic

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

class CourseDetailView(generic.DetailView):
    model = Course
    template_name = "course_detail.html"
