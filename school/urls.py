# from django.urls import path
# from .views import *
#
# urlpatterns = [
#     path('', index, name='home'),
#     path('tutors/', tutors, name='for_tutors'),
#     path('blog/', blog, name='blog'),
#     path('info/', info, name='info'),
#     path('recording/', recording, name='recording'),
#]

from django.urls import path
from .views import *

urlpatterns = [
    path('courselist/', CourseAPIList.as_view()),
    path('courselist/<int:pk>/', CourseAPIUpdate.as_view()),
    path('coursedetail/<int:pk>/', CourseAPIDetailView.as_view()),
]
