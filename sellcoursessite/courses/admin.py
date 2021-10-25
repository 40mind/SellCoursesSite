from django.contrib import admin
from .models import Direction, Course

# Register your models here.

admin.site.register(Direction)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction', 'firstdate', 'info')
    list_filter = ('firstdate', )
    search_fields = ('name__startswith', )

admin.site.register(Course, CourseAdmin)
