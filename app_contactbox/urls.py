#!/usr/bin/python3.7
from django.urls import path
from app_contactbox import views

urlpatterns = [
    path('', views.AllContactsView.as_view(), name='all-contacts'),
    path('create_person/', views.CreatePersonView.as_view(), name='create-person'),
    path('create_address/', views.CreateAddressView.as_view(), name='create-address'),
    path('create_group/', views.CreateGroupView.as_view(), name='create-group'),
    path('create_phone/', views.CreatePhoneView.as_view(), name='create-phone'),
    path('create_email/', views.CreateEmailView.as_view(), name='create-email'),
    path('person_details/<int:pk>', views.PersonDetailsView.as_view(), name='person-details'),
    path('update_person/<int:pk>', views.EditPersonView.as_view(), name='update-person'),
    path('delete_person/<int:pk>', views.DeletePersonView.as_view(), name='delete-person'),
]
