from django.db import models


PHONE_TYPES = {
    1: 'mobile',
    2: 'home',
    3: 'work',
    4: 'other'
}


EMAIL_TYPES = {
    1: 'private',
    2: 'work',
    3: 'other',
}


class Person(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    surname = models.CharField(max_length=64, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    address = models.ForeignKey('Address', null=True, blank=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField('Group', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}{" " + self.surname if self.surname else None}'


class Address(models.Model):
    town = models.CharField(max_length=64, null=False, blank=False)
    street = models.CharField(max_length=64, null=True, blank=True)
    house_no = models.CharField(max_length=8, null=True, blank=True)
    apartment_no = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f'{self.town}{", " + self.street if self.street else None} ' \
               f'{" " + self.house_no if self.house_no else None}' \
               f'{"/" + self.apartment_no if self.apartment_no else None}'


class Phone(models.Model):
    number = models.IntegerField(max_length=9, null=True, blank=True)
    phone_type = models.CharField(choices=PHONE_TYPES, null=True, blank=True)
    person = models.ForeignKey('Person', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class Email(models.Model):
    email = models.CharField(max_length=64, null=True, blank=True)
    email_type = models.CharField(choices=EMAIL_TYPES, null=True, blank=True)
    person = models.ForeignKey('Person', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class Group(models.Model):
    group_name = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return self.group_name
