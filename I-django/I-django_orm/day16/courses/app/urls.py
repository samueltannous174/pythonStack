from . import views
from django.urls import path
urlpatterns=[
    path('', views.index),
    path('add_course', views.addCourse),
    path('destroy/<int:course_id>', views.deleteCourse),
    path('delete', views.destroyCourse),

]