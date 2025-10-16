from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('show_register', views.registerShow),
    path('register', views.register),
    path('all_users', views.allUsers),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('edit_show', views.editShow),
    path('edit/<int:user_id>', views.editUser),

]
