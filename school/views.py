from django.shortcuts import render
from rest_framework import generics

from school.models import *
from school.serializers import CourseSerializer, BlogSerializer, StudentSerializer
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from . import worksheet


class CourseViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class BlogViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class StudentViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RecordAPIView(APIView):
    def post(self, request):
        subject = request.data['subject']
        course = request.data['class']
        time = request.data['time']
        email = request.data['email']

        worksheet.WorkSheet().append_request(subject, course, time, email.lower(), )

        record = {'subject': subject, 'class': course, "time": time, "email": email, }
        return Response({"post": record})

# class RecordViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     queryset = Record.objects.all()
#     serializer_class = RecordSerializer
