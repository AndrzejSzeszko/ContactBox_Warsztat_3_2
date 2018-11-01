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

    def get(self, request):
        person_form = PersonForm()
        return render(request, 'app_contactbox/new-person.html', {'person_form': person_form})
    
    def post(self, request):
        data = {
            'name': request.POST.get('name'),
            'surname': request.POST.get('surname'),
            'description': request.POST.get('description'),
            'address': Address.objects.filter(id=request.POST.get('address') if request.POST.get('address') else None).first(),
        }

        Person.objects.create(**data).groups.set(request.POST.get('groups') if request.POST.get('groups') else [])

        return redirect('new-person')


class NewAddressView(View):

    def get(self, request, info=''):
        address_form = AddressForm()
        context = {
            'address_form': address_form,
            'info': info
        }
        return render(request, 'app_contactbox/new-address.html', context)

    def post(self, request):
        address_data = AddressForm(request.POST)
        if address_data.is_valid():
            try:
                Address.objects.create(**address_data.cleaned_data)
                info = 'success'
            except IntegrityError:
                info = 'fail'
            return redirect('new-address-info', info)
