from django.contrib import admin
from django.urls import path, include

from school.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'course', CourseViewSet)
router.register(r'blog', BlogViewSet)
router.register(r'student', StudentViewSet)


urlpatterns = [
    path('', include(router.urls)),  # http://127.0.0.1:8000/course/<pk>
    path('recording/', RecordAPIView.as_view()),
]
