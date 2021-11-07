from django.contrib import admin
from .models import Direction, Course, Person

# Register your models here.

admin.site.register(Direction)
admin.site.register(Person)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction', 'firstdate', 'info')
    list_filter = ('firstdate', )
    search_fields = ('name__startswith', )

admin.site.register(Course, CourseAdmin)
