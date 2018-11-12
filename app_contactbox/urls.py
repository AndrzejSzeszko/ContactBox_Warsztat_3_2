#!/usr/bin/python3.7
from django.urls import path
from app_contactbox import views

urlpatterns = [
    path('', views.AllContactsView.as_view(), name='all-contacts'),
    path('new_person/', views.NewPersonView.as_view(), name='new-person'),
    path('new_person/<str:info>/', views.NewPersonView.as_view(), name='new-person-info'),
    path('create_address/', views.CreateAddressView.as_view(), name='create-address'),
    path('new_group/', views.NewGroupView.as_view(), name='new-group'),
    path('new_group/<str:info>', views.NewGroupView.as_view(), name='new-group-info'),
    path('new_phone/', views.NewPhoneView.as_view(), name='new-phone'),
    path('new_phone/<str:info>', views.NewPhoneView.as_view(), name='new-phone-info'),
    path('new_email/', views.NewEmailView.as_view(), name='new-email'),
    path('new_email/<str:info>', views.NewEmailView.as_view(), name='new-email-info'),
    path('person_details/<int:pk>', views.PersonDetailsView.as_view(), name='person-details'),
    path('edit_person/<int:pk>', views.EditPersonView.as_view(), name='edit-person'),
    path('delete_person/<int:pk>', views.DeletePersonView.as_view(), name='delete-person'),
]
