from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('add_book', views.addBook),
    path('books/<int:book_id>', views.viewBook),
    path('delete_book/<int:book_id>', views.deleteBook),
    path('update_book/<int:book_id>', views.updateBook),
    path('unfavorite/<int:user_id>/<int:book_id>', views.unfavoriteBook),
    path('favorite/<int:user_id>/<int:book_id>', views.favoriteBook),
]

