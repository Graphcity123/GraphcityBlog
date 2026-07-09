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
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^content/(?P<path>.*)$', serve, {'document_root': settings.CONTENT_DIR}),
    ]
