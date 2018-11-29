from django.shortcuts import (render,
                              redirect)
from django.views import View
from django.views.generic import (DetailView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView)
from django.views.generic.edit import FormView
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
from django.urls import reverse_lazy
from django.contrib import messages


class AllContactsView(View):
    def get(self, request):
        persons = Person.objects.all().order_by('surname', 'name')
        return render(request, 'app_contactbox/all_contacts.html', {'persons': persons})


class CreateContactView(View):
    def get(self, request):
        ctx = {
            'person_form': PersonForm(),
            'phone_form': PhoneForm(),
            'email_form': EmailForm()
        }
        return render(request, 'app_contactbox/contact_create.html', ctx)

    def post(self, request):
        person_form = PersonForm(request.POST)

        phone_forms = {}
        for index, number in enumerate(request.POST.getlist('number')):
            phone_forms[f'phone_form_{index}'] = PhoneForm({
                'number': number,
                'phone_type': request.POST.getlist('phone_type')[index]
            })
            
        email_forms = {}
        for index, email in enumerate(request.POST.getlist('email')):
            email_forms[f'email_form_{index}'] = EmailForm({
                'email': email,
                'email_type': request.POST.getlist('email_type')[index]
            })

        phones_and_emails_forms = dict(**phone_forms, **email_forms)
        if person_form.is_valid() and all([form.is_valid() for form in phones_and_emails_forms.values()]):
            current_person = person_form.save()
            for name, form in phones_and_emails_forms.items():
                form.cleaned_data['person'] = current_person
                if 'phone' in name:
                    Phone.objects.create(**form.cleaned_data)
                elif 'email' in name:
                    Email.objects.create(**form.cleaned_data)

            messages.success(request, f'Contact for {current_person} successfully created')
            return redirect('person-details', current_person.pk)
        else:
            messages.error(request, 'Person creation failed.')
            return redirect('create-contact')


    # def get_success_url(self):
    #     return reverse_lazy('person-details', kwargs={'pk': self.object.pk})
    #
    # def form_valid(self, form):
    #     data = form.cleaned_data
    #     name = data.get('name')
    #     surname = data.get('surname')
    #     messages.success(self.request, f'Person {name} {surname} successfully created.')
    #
    #     return super().form_valid(form)
    #
    # def form_invalid(self, form):
    #     messages.error(self.request, f'Person creation failed.')
    #     return super().form_invalid(form)


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
    success_url = reverse_lazy('create-group')
    template_name_suffix = '_create'

    def form_valid(self, form):
        messages.success(self.request, f'Group {form.cleaned_data.get("group_name")} successfully created.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f'Group creation failed.')
        return super().form_invalid(form)


class CreatePhoneView(CreateView):
    form_class = PhoneForm
    model = Phone
    success_url = reverse_lazy('create-phone')
    template_name_suffix = '_create'

    def form_valid(self, form):
        messages.success(self.request, f'Phone {form.cleaned_data.get("number")} successfully created.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f'Phone creation failed.')
        return super().form_invalid(form)


class CreateEmailView(CreateView):
    form_class = EmailForm
    model = Email
    success_url = reverse_lazy('create-email')
    template_name_suffix = '_create'

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
