from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class Student_Admin(admin.ModelAdmin):
    list_display = ('pk', 'name','amount_courses')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('amount_courses',)# создаёт фильтр по этим значениям. Которым можно пользоваться в админ панели на сайте 

admin.site.register(Student, Student_Admin)


class Teacher_Admin(admin.ModelAdmin):
    list_display = ('pk', 'name','education','specialization','work_experience','amount_courses')
    list_display_links = ('name',)
    search_fields = ('name','specialization')
    list_filter = ('specialization', 'work_experience','amount_courses')# создаёт фильтр по этим значениям. Которым можно пользоваться в админ панели на сайте 

admin.site.register(Teacher, Teacher_Admin)

class Course_Admin(admin.ModelAdmin):
    list_display = ('pk', 'subject','grade','teacher','time_lesson','amount_studens','amount_places','is_full')# добавил поля для отображения 'amount_studens','amount_places','is_full'
    list_display_links = ('subject',)
    search_fields = ('subject','grade','teacher')
    list_filter = ('subject', 'grade','is_full','amount_places')# создаёт фильтр по этим значениям. Которым можно пользоваться в админ панели на сайте 
    list_editable = ('is_full',)# позволяет редактировать поля не заходя во внутрь

admin.site.register(Course, Course_Admin)

class Blog_Admin(admin.ModelAdmin):
    list_display = ('pk', 'title','content','created_at','update_at','is_published','photo')
    list_display_links = ('title',)
    search_fields = ('subject','grade','teacher')
    list_editable = ('is_published',)# если это работает так как я думаю, то она должна статья будет убираться если убрать эту галочку и наоборот
    list_filter = ('is_published', 'created_at')
    
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img scr=" {obj.photo.url}" width=75>')
        else:
            return '-'

admin.site.register(Blog, Blog_Admin)
