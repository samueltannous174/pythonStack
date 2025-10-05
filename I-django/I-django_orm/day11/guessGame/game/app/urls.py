from . import views
from django.urls import path



urlpatterns = [
    path('', views.index),
    path('submitted', views.submitted),
    path ('reset', views.reset),
]
