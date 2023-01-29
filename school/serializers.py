from rest_framework import serializers
from .models import Course, Blog, RequestList


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class RequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestList
        fields = '__all__'

