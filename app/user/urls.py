"""
URLs for the user API
"""
from django.contrib.auth import views as auth_views
from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
