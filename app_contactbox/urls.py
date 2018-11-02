#!/usr/bin/python3.7
from django.urls import path
from app_contactbox import views

urlpatterns = [
    path('', views.AllContactsView.as_view(), name='all-contacts'),
    path('new-person/', views.NewPersonView.as_view(), name='new-person'),
    path('new-person/<str:info>/', views.NewPersonView.as_view(), name='new-person-info'),
    path('new-address/', views.NewAddressView.as_view(), name='new-address'),
    path('new-address/<str:info>/', views.NewAddressView.as_view(), name='new-address-info'),
    path('new-group/', views.NewGroupView.as_view(), name='new-group'),
    path('new-group/<str:info>', views.NewGroupView.as_view(), name='new-group-info'),
    path('new-phone/', views.NewPhoneView.as_view(), name='new-phone'),
    path('new-phone/<str:info>', views.NewPhoneView.as_view(), name='new-phone-info'),
]
