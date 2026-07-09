"""
URL configuration.
"""
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<slug>/', views.article, name='article'),
    path('project/<name>/', views.project, name='project'),
    path('about/', views.about, name='about'),
]
