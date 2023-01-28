from django.contrib import admin
from django.urls import path, include

from school.views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'course', CourseViewSet)
router.register(r'blog', BlogViewSet)


urlpatterns = [
    path('', include(router.urls)),  # http://127.0.0.1:8000/course/<pk>
]
#
#
# from django.urls import path
# from .views import *
#
# urlpatterns = [
#     path('courselist/', CourseAPIList.as_view()),
#     path('courselist/<int:pk>/', CourseAPIUpdate.as_view()),
#     path('coursedetail/<int:pk>/', CourseAPIDetailView.as_view()),
#     path('bloglist/', BlogAPIList.as_view()),
#     path('bloglist/<int:pk>/', BlogAPIUpdate.as_view()),
#     path('blogdetail/<int:pk>/', BlogAPIDetailView.as_view()),
# ]
