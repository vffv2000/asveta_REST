from django.shortcuts import render
from rest_framework import generics

from school.models import *
from school.serializers import CourseSerializer, BlogSerializer
from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet


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

# class CourseAPIList(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseAPIUpdate(generics.UpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer


# class BlogAPIList(generics.ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#
# class BlogAPIUpdate(generics.UpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#
# class BlogAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

