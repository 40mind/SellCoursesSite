from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^admin/directions/$', views.admin_directions, name='admin_directions'),
    url(r'^admin/courses/$', views.admin_courses, name='admin_courses'),
    url(r'^admin/people/$', views.admin_people, name='admin_people'),
    url(r'^detail/(?P<pk>\d+)$', views.CourseDetailView.as_view(), name='course_detail'),
    url(r'^record/$', views.PersonCreate.as_view(), name='record_on_course'),
]
