from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('add_message', views.addMessage),
    path('add_comment/<int:message_id>', views.addComment),
    path('delete_message/<int:message_id>', views.deleteMessage),
]

