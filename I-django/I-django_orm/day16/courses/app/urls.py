from . import views
from django.urls import path
urlpatterns=[
    path('', views.index),
    path('add_course', views.addCourse),
    path('delete/<int:course_id>', views.deleteCourse),

]