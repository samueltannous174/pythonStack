
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('add_book', views.addBook),
    path('books/<int:book_id>', views.viewBook),
    path('add_author_to_book/<int:book_id>', views.addAuthorToBook),
]