from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    #path('', views.home_page, name='home_page'),
    url(r'^$', views.home_page, name='home_page'),
    url(r'^(?P<pk>\d+)$', views.CourseDetailView.as_view(), name='course_detail'),
]