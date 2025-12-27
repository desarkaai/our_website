"""
URL configuration for web application.
"""
from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about-us/', views.about_view, name='about_us'),
    path('solutions/', views.placeholder_view, name='solutions'),
    path('projects/', views.placeholder_view, name='projects'),
    path('newsroom/', views.placeholder_view, name='newsroom'),
    path('careers/', views.placeholder_view, name='careers'),
    path('connect/', views.connect_view, name='connect'),
]