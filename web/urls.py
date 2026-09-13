from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about-us/', views.about_view, name='about_us'),
    path('solutions/', views.solutions_view, name='solutions'),
    path('solutions/<slug:slug>/', views.solution_detail_view, name='solution_detail'),
    path('projects/', views.projects_view, name='projects'),
    path('projects/<slug:slug>/', views.case_study_view, name='case_study'),
    path('newsroom/', views.placeholder_view, name='newsroom'),
    path('careers/', views.placeholder_view, name='careers'),
    path('connect/', views.connect_view, name='connect'),
]