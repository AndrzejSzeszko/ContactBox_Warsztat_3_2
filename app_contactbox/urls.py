#!/usr/bin/python3.7
from django.urls import path
from app_contactbox import views

urlpatterns = [
    path('/', views.HomeView.as_view(), name='home'),
]
