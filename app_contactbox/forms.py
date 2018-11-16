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
            'description': forms.Textarea,
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        exclude = ['person']


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
