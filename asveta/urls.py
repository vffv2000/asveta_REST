# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('', include('school.urls')),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path

from school.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/courselist/', CourseAPIList.as_view()),
    path('api/v1/courselist/<int:pk>/', CourseAPIUpdate.as_view()),
    path('api/v1/coursedetail/<int:pk>/', CourseAPIDetailView.as_view()),
]