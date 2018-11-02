#!/usr/bin/python3.7
from django.urls import path
from app_contactbox import views

urlpatterns = [
    path('', views.AllContactsView.as_view(), name='all-contacts'),
    path('new-person/', views.NewPersonView.as_view(), name='new-person'),
    path('new-person/<str:info>/', views.NewPersonView.as_view(), name='new-person-info'),
    path('new-address/', views.NewAddressView.as_view(), name='new-address'),
    path('new-address/<str:info>/', views.NewAddressView.as_view(), name='new-address-info'),
]
