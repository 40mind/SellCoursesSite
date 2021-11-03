from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^admin/directions/$', views.admin_directions, name='admin_directions'),
    url(r'^admin/courses/$', views.admin_courses, name='admin_courses'),
    url(r'^admin/people/$', views.admin_people, name='admin_people'),
    url(r'^admin/courses/detail/(?P<pk>\d+)$', views.AdminCourseDetailView.as_view(), name='admin_course_detail'),
    url(r'^admin/people/detail/(?P<pk>\d+)$', views.AdminPersonDetailView.as_view(), name='admin_person_detail'),
    url(r'^admin/directions/create/$', views.AdminDirectionCreate.as_view(), name='admin_directions_create'),
    url(r'^admin/directions/update/(?P<pk>\d+)$', views.AdminDirectionUpdate.as_view(), name='admin_direction_update'),
    url(r'^admin/directions/delete/(?P<pk>\d+)$', views.AdminDirectionDelete.as_view(), name='admin_direction_delete'),
    url(r'^admin/courses/create/$', views.AdminCourseCreate.as_view(), name='admin_courses_create'),
    url(r'^admin/courses/update/(?P<pk>\d+)$', views.AdminCourseUpdate.as_view(), name='admin_course_update'),
    url(r'^admin/courses/delete/(?P<pk>\d+)$', views.AdminCourseDelete.as_view(), name='admin_course_delete'),
    url(r'^admin/people/create/$', views.AdminPersonCreate.as_view(), name='admin_people_create'),
    url(r'^admin/people/update/(?P<pk>\d+)$', views.AdminPersonUpdate.as_view(), name='admin_person_update'),
    url(r'^admin/people/delete/(?P<pk>\d+)$', views.AdminPersonDelete.as_view(), name='admin_person_delete'),
    url(r'^detail/(?P<pk>\d+)$', views.CourseDetailView.as_view(), name='course_detail'),
    url(r'^record/$', views.PersonCreate.as_view(), name='record_on_course'),
]
