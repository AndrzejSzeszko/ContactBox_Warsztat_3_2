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


class HomeView(View):

    def get(self, request):
        persons = Person.objects.all().order_by('surname', 'name')
        return render(request, 'app_contactbox/home.html', {'persons': persons})


class NewPersonView(View):

    def get(self, request):
        person_form = PersonForm()
        return render(request, 'app_contactbox/new_person.html', {'person_form': person_form})
