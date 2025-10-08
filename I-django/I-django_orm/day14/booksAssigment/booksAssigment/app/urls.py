
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('add_book', views.addBook),
    path('books/<int:book_id>', views.viewBook),
    path('add_author_to_book/<int:book_id>', views.addAuthorToBook),
    path('authors', views.indexAuthors),
    path('add_author', views.addAuthor),
    path('authors/<int:author_id>', views.viewAuthor),
    path('add_book_to_author/<int:author_id>', views.addBookToAuthor)


]