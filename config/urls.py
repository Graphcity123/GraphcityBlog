"""
URL configuration.
"""
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<slug>/', views.article, name='article'),
    path('project/<name>/', views.project, name='project'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('archive/', views.archive, name='archive'),
    path('archive/<str:tag>/', views.archive, name='archive_tag'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/page/<int:pg>/', views.article_list, name='article_list_page'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/page/<int:pg>/', views.project_list, name='project_list_page'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^content/(?P<path>.*)$', serve, {'document_root': settings.CONTENT_DIR}),
    ]
