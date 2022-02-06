from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'price')

# Register your models here.
admin.site.register(Course, CourseAdmin)