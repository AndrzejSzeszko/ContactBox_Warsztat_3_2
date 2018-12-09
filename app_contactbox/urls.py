#!/usr/bin/python3.7
from django.urls import path
from app_contactbox import views

urlpatterns = [
    path('', views.AllContactsView.as_view(), name='all-contacts'),
    path('create_contact/', views.CreateContactView.as_view(), name='create-contact'),
    path('create_address/', views.CreateAddressView.as_view(), name='create-address'),
    path('create_group/', views.CreateGroupView.as_view(), name='create-group'),
    path('create_phone/', views.CreatePhoneView.as_view(), name='create-phone'),
    path('create_email/', views.CreateEmailView.as_view(), name='create-email'),
    path('person_details/<int:pk>', views.PersonDetailsView.as_view(), name='person-details'),
    path('update_contact/<int:pk>', views.EditContactView.as_view(), name='update-contact'),
    path('delete_person/<int:pk>', views.DeletePersonView.as_view(), name='delete-person'),
]
