#!/usr/bin/python3.7
from django import forms
from .models import (Person,
                     Address,
                     Group,
                     Phone,
                     Email)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'groups': forms.CheckboxSelectMultiple,
            'description': forms.Textarea
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class PhoneForm(forms.Form):
    number = forms.CharField(label='Number:', max_length=9)
    phone_type = forms.ChoiceField(label='Phone type:', choices=Phone.PHONE_TYPES)
    person = forms.ModelChoiceField(label='Person:', queryset=Person.objects.all(), required=False)


class EmailForm(forms.Form):
    email = forms.CharField(label='Email:', max_length=64)
    email_type = forms.ChoiceField(label='Email type:', choices=Email.EMAIL_TYPES)
    person = forms.ModelChoiceField(label='Person:', queryset=Person.objects.all(), required=False)


class GroupForm(forms.Form):
    group_name = forms.CharField(label='Name:', max_length=32)
