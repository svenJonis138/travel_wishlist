from django.urls import path
from . import views
""" directs browser to the different pages """

urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('about', views.about, name='about'),
    path('place/<int:place_pk>/was_visited', views.place_was_visited, name='place_was_visited'),
    path('visited', views.places_visited, name='places_visited'),
    path('place/<int:place_pk>/was_visited/', views.place_was_visited, name='place_was_visited'),
    path('place/<int:place_pk>', views.place_details, name='place_details'),
    path('place/<int:place_pk>/delete', views.delete_place, name='delete_place')
]