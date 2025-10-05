from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from app.views import index, submitted
urlpatterns = [
    path('', index),
    path('submitted', submitted),
]