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
            'address_form': AddressForm(),
            'group_form': GroupForm(),
            'phone_form': PhoneForm(),
            'email_form': EmailForm()
        }
        return render(request, 'app_contactbox/contact_create.html', ctx)

    def post(self, request):
        person_form = PersonForm(request.POST)

        group_forms = {}
        for index, group_name in enumerate(request.POST.getlist('group_name')):
            group_forms[f'group_form_{index}'] = GroupForm({
                'group_name': group_name
            })

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

        all_forms = dict(**phone_forms, **email_forms, **group_forms)

        if request.POST.get('town'):
            all_forms['address_form'] = AddressForm(request.POST)

        if person_form.is_valid() and all(form.is_valid() for form in all_forms.values()):
            current_person = person_form.save()
            for name, form in all_forms.items():
                if 'address' in name:
                    current_address = form.save()
                    current_person.address = current_address
                    current_person.save()
                elif 'group' in name:
                    current_group = form.save()
                    current_person.groups.add(current_group)
                elif 'email' in name or 'phone' in name:
                    form.cleaned_data['person'] = current_person
                    if 'email' in name:
                        Email.objects.create(**form.cleaned_data)
                    elif 'phone' in name:
                        Phone.objects.create(**form.cleaned_data)

            messages.success(request, f'Contact for {current_person} successfully created')
            return redirect('person-details', current_person.pk)
        else:
            messages.error(request, 'Person creation failed.')
            return redirect('create-contact', )


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


class EditContactView(View):
    def get(self, request, pk):
        current_person = Person.objects.get(pk=pk)
        ctx = {
            'current_person': current_person,
            'person_form': PersonForm(instance=current_person),
            'address_form': AddressForm(instance=current_person.address),
            'group_form': GroupForm(),
            'phone_forms': [PhoneForm(instance=phone) for phone in current_person.phone_set.all()],
            'email_forms': [EmailForm(instance=email) for email in current_person.email_set.all()]
        }
        return render(request, 'app_contactbox/contact_update.html', ctx)

    def post(self, request, pk):
        current_person = Person.objects.get(pk=pk)
        person_form = PersonForm(request.POST, instance=current_person)

        group_forms = {}
        for index, group_name in enumerate(request.POST.getlist('group_name')):
            group_forms[f'group_form_{index}'] = GroupForm({
                'group_name': group_name
            })

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

        all_forms = dict(**phone_forms, **email_forms, **group_forms)

        if request.POST.get('town'):
            all_forms['address_form'] = AddressForm(request.POST)

        if person_form.is_valid() and all(form.is_valid() for form in all_forms.values()):
            current_person = person_form.save()
            Phone.objects.filter(person=current_person).delete()
            Email.objects.filter(person=current_person).delete()
            for name, form in all_forms.items():
                if 'address' in name:
                    current_address = form.save()
                    current_person.address = current_address
                    current_person.save()
                elif 'group' in name:
                    current_group = form.save()
                    current_person.groups.add(current_group)
                elif 'email' in name or 'phone' in name:
                    form.cleaned_data['person'] = current_person
                    if 'email' in name:
                        Email.objects.create(**form.cleaned_data)
                    elif 'phone' in name:
                        Phone.objects.create(**form.cleaned_data)

            messages.success(request, f'Contact for {current_person} successfully updated')
            return redirect('person-details', current_person.pk)
        else:
            messages.error(request, 'Person update failed.')
            return redirect('create-contact', )


class DeletePersonView(DeleteView):
    model = Person
    success_url = reverse_lazy('all-contacts')
    template_name_suffix = '_delete'

    def delete(self, request, *args, **kwargs):
        messages.success(request, f'Person {self.get_object()} successfully deleted.')
        return super().delete(request)
