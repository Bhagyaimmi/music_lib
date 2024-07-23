from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('folder/new/', views.FolderCreateView.as_view(), name='folder-create'),
    path('track/new/', views.MusicCreateView.as_view(), name='music-create'),
]
