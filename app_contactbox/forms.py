#!/usr/bin/python3.7
from django import forms
from .models import (Person,
                     Address,
                     Group,
                     Phone,
                     Email)


class PersonForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=64)
    surname = forms.CharField(label='Surname:', max_length=64, empty_value=None, required=False)
    description = forms.CharField(label='Description:', max_length=256, empty_value=None, required=False)
    # photo = forms.ImageField(label='Upload photo:', upload_to='photos')
    address = forms.ModelChoiceField(label='Address:', queryset=Address.objects.all(), required=False)
    groups = forms.ModelMultipleChoiceField(label='Groups:', queryset=Group.objects.all(), required=False)


class AddressForm(forms.Form):
    town = forms.CharField(label='Town:', max_length=64)
    street = forms.CharField(label='Street:', max_length=64, empty_value=None, required=False)
    house_no = forms.CharField(label='House No:', max_length=8, empty_value=None, required=False)
    apartment_no = forms.CharField(label='Apartment No:', max_length=8, empty_value=None, required=False)
    

class PhoneForm(forms.Form):
    number = forms.CharField(label='Number:', max_length=9)
    phone_type = forms.ChoiceField(label='Phone type:', choices=Phone.PHONE_TYPES, required=False)
    person = forms.ModelChoiceField(label='Person:', queryset=Person.objects.all())


class EmailForm(forms.Form):
    email = forms.CharField(label='Email:', max_length=64)
    email_type = forms.ChoiceField(label='Email type:', choices=Email.EMAIL_TYPES, required=False)
    person = forms.ModelChoiceField(label='Person:', queryset=Person.objects.all())


class GroupForm(forms.Form):
    group_name = forms.ChoiceField(label='Name:', max_length=32)
