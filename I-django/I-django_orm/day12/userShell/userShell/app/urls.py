from app import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('add_users', views.add),
    
]
