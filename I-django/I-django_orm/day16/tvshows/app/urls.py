from django.urls import path
from . import views
urlpatterns=[
    path('', views.index),
    path('shows/addNew', views.addNew),
    path('shows/addNewShow', views.addNewShow),
    path('shows/<int:show_id>', views.show),
    path('shows/<int:show_id>/edit', views.editShow),
    path('shows/<int:show_id>/edits', views.editShows),
    path('shows', views.showAll),
    path('shows/<int:show_id>/delete', views.deleteShow),
]