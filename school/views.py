from django.shortcuts import render
from rest_framework import generics

from school.models import *
from school.serializers import CourseSerializer


class CourseAPIList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIUpdate(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# def index(request):
#     return render(request, 'school/index.html')
#
# def tutors(request):
#     return render(request, 'school/for_tutors.html')
#
# def blog(request):
#     return render(request, 'school/blog.html')
#
# def info(request):
#     return render(request, 'school/info.html')
#
# def recording(request):
#     return render(request, 'school/recording.html')
#



