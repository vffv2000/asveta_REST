from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class Student_Admin(admin.ModelAdmin):
    list_display = ('name','amount_courses')
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Student, Student_Admin)


class Teacher_Admin(admin.ModelAdmin):
    list_display = ('name','education','specialization','work_experience','amount_courses')
    list_display_links = ('name',)
    search_fields = ('name','specialization')

admin.site.register(Teacher, Teacher_Admin)

class Course_Admin(admin.ModelAdmin):
    list_display = ('subject','grade','teacher','time_lesson')
    list_display_links = ('subject',)
    search_fields = ('subject','grade','teacher')

admin.site.register(Course, Course_Admin)

class Blog_Admin(admin.ModelAdmin):
    list_display = ('title','content','update_at','is_published','photo')
    list_display_links = ('title',)
    search_fields = ('subject','grade','teacher')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img scr=" {obj.photo.url}" width=75>')
        else:
            return '-'

admin.site.register(Blog, Blog_Admin)
