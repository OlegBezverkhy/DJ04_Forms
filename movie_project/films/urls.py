from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movie_list/', views.movie_list, name='movie_list'),
]