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


def generic_get(request, name, form, info):
    """generic get function for all class based views"""
    context = {
        'person_form': form(),
        'info': info
    }
    return render(request, f'app_contactbox/new-{name}.html', context)


def generic_post(request, name, form, model):
    """generic post function for all class based views"""
    current_form = form(request.POST)
    if current_form.is_valid():
        try:
            model.objects.create(**current_form.cleaned_data)
            info = 'Success'
        except IntegrityError:
            info = 'IntegrityError'
    else:
        info = 'InvalidInput'
    return redirect(f'new-{name}-info', info)


class AllContactsView(View):

    def get(self, request):
        persons = Person.objects.all().order_by('surname', 'name')
        return render(request, 'app_contactbox/all-contacts.html', {'persons': persons})


class NewPersonView(View):

    def get(self, request, info=''):
        return generic_get(request, 'person', PersonForm, info)
    
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
        return generic_get(request, 'address', AddressForm, info)

    def post(self, request):
        return generic_post(request, 'address', AddressForm, Address)


class NewGroupView(View):

    def get(self, request, info=''):
        return generic_get(request, 'group', GroupForm, info)

    def post(self, request):
        return generic_post(request, 'group', GroupForm, Group)


class NewPhoneView(View):

    def get(self, request, info=''):
        return generic_get(request, 'phone', PhoneForm, info)

    def post(self, request):
        return generic_post(request, 'phone', PhoneForm, Phone)


class NewEmailView(View):

    def get(self, request, info=''):
        return generic_get(request, 'email', EmailForm, info)

    def post(self, request):
        return generic_post(request, 'email', EmailForm, Email) #todo add email validation
