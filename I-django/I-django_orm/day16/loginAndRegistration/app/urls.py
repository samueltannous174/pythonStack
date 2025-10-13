import path 
from . import views

urlpatterns = [
    path('', views.index),
]