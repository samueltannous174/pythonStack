
from django.urls import path
from . import views 
from app import views

urlpatterns = [
    path('', views.counter),
    path('counter', views.counter)
]
