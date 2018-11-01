#!/usr/bin/python3.7
from django.urls import path
from app_contactbox import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('new-person/', views.NewPersonView.as_view(), name='new_person'),
]
