from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('add_game', views.addGame),
    path('sort/', views.sortByGenere),
    path('game/<int:game_id>', views.showGame),
    path('favorite/<int:game_id>', views.addToFavorites),
    path('update_game/<int:game_id>', views.updateGame),
    path('update_game2/<int:game_id>', views.updateGame2),
    path('delete_game/<int:game_id>', views.deleteGame),

]

