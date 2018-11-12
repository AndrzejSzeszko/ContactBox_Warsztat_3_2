from django.shortcuts import (render,
                              redirect)
from django.views import View
from django.views.generic import (DetailView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView)
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
from django.urls import reverse_lazy
from django.contrib import messages


def generic_get(request, name, form, info):
    """generic get function for all class based views"""
    context = {
        f'{name}_form': form(),
        'info': info
    }
    return render(request, f'app_contactbox/new_{name}.html', context)


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
        return render(request, 'app_contactbox/all_contacts.html', {'persons': persons})


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


class CreateAddressView(CreateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('create-address')
    template_name_suffix = '_create'

    def form_valid(self, form):
        data = form.cleaned_data
        town = data.get('town')
        street = data.get('street')
        house_no = data.get('house_no')
        apartment_no = data.get('apartment_no')
        messages.success(self.request, f'Address {town}, {street} {house_no}/{apartment_no} successfully created.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f'Address creation failed.')
        return super().form_invalid(form)


class CreateGroupView(CreateView):
    form_class = GroupForm
    model = Group
    template_name_suffix = '_create'
    success_url = reverse_lazy('create-group')

    def form_valid(self, form):
        messages.success(self.request, f'Group {form.cleaned_data.get("group_name")} successfully created.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f'Group creation failed.')
        return super().form_invalid(form)


class CreatePhoneView(CreateView):
    form_class = PhoneForm
    model = Phone
    template_name_suffix = '_create'
    success_url = reverse_lazy('create-phone')

    def form_valid(self, form):
        messages.success(self.request, f'Phone {form.cleaned_data.get("number")} successfully created.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f'Phone creation failed.')
        return super().form_invalid(form)


class CreateEmailView(CreateView):
    form_class = EmailForm
    model = Email
    template_name_suffix = '_create'
    success_url = reverse_lazy('create-email')

    def form_valid(self, form):
        messages.success(self.request, f'Email {form.cleaned_data.get("email")} successfully created.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f'Email creation failed.')
        return super().form_invalid(form)


class PersonDetailsView(DetailView):
    model = Person
    template_name_suffix = '_details'


class EditPersonView(UpdateView):
    form_class = PersonForm
    model = Person
    template_name_suffix = '_update'

    def get_success_url(self):
        person_pk = self.object.pk
        return reverse_lazy('person-details', kwargs={'pk': person_pk})

    def form_valid(self, form):
        messages.success(self.request, f'Person\'s {self.object} data successfully updated.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f'Person\'s {self.object} data update failed.')
        return super().form_invalid(form)


class DeletePersonView(DeleteView):
    model = Person
    success_url = reverse_lazy('all-contacts')
    template_name_suffix = '_delete'

    def delete(self, request, *args, **kwargs):
        messages.success(request, f'Person {self.get_object()} successfully deleted.')
        return super().delete(request)
