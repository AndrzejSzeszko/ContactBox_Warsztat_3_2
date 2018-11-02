from django.shortcuts import (render,
                              redirect)
from django.views import View
from .models import (Person,
                     Address,
                     Group,
                     Phone,
                     Email)
from .forms import (PersonForm,
                    AddressForm,
                    PhoneForm,
                    EmailForm,
                    GroupForm)
from django.db import IntegrityError


class AllContactsView(View):

    def get(self, request):
        persons = Person.objects.all().order_by('surname', 'name')
        return render(request, 'app_contactbox/all-contacts.html', {'persons': persons})


class NewPersonView(View):

    def get(self, request, info=''):
        person_form = PersonForm()
        context = {
            'person_form': person_form,
            'info': info
        }
        return render(request, 'app_contactbox/new-person.html', context)
    
    def post(self, request):
        person_form = PersonForm(request.POST)
        if person_form.is_valid():
            data = person_form.cleaned_data
            groups = data.pop('groups')
            new_person = Person.objects.create(**data)
            new_person.groups.set(groups)
            info = 'Success'
        else:
            info = 'InvalidInput'
        return redirect('new-person-info', info)


class NewAddressView(View):

    def get(self, request, info=''):
        address_form = AddressForm()
        context = {
            'address_form': address_form,
            'info': info
        }
        return render(request, 'app_contactbox/new-address.html', context)

    def post(self, request):
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            try:
                Address.objects.create(**address_form.cleaned_data)
                info = 'Success'
            except IntegrityError:
                info = 'IntegrityError'
        else:
            info = 'InvalidInput'
        return redirect('new-address-info', info)


class NewGroupView(View):

    def get(self, request, info=''):
        group_form = GroupForm()
        context = {
            'group_form': group_form,
            'info': info
        }
        return render(request, 'app_contactbox/new-group.html', context)

    def post(self, request):
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            try:
                Group.objects.create(**group_form.cleaned_data)
                info = 'Success'
            except IntegrityError:
                info = 'IntegrityError'
        else:
            info = 'InvalidInput'
        return redirect('new-group-info', info)


class NewPhoneView(View):

    def get(self, request, info=''):
        phone_form = PhoneForm()
        context = {
            'phone_form': phone_form,
            'info': info
        }
        return render(request, 'app_contactbox/new-phone.html', context)

    def post(self, request):
        phone_form = PhoneForm(request.POST)
        if phone_form.is_valid():
            try:
                Phone.objects.create(**phone_form.cleaned_data)
                info = 'Success'
            except IntegrityError:
                info = 'IntegrityError'
        else:
            info = 'InvalidInput'
        return redirect('new-phone-info', info)
