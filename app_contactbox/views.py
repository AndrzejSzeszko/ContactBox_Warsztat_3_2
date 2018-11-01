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
    
    def post(self, request):
        
        data = {
            'name': request.POST.get('name'),
            'surname': request.POST.get('surname'),
            'description': request.POST.get('description'),
            'address': Address.objects.filter(id=request.POST.get('address') if request.POST.get('address') else None).first(),
        }

        Person.objects.create(**data).groups.set(request.POST.get('groups') if request.POST.get('groups') else [])
        
        return redirect('new_person')
