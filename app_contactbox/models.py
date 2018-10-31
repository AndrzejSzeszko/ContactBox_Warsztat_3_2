from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    # photo = models.ImageField(upload_to='photos')
    address = models.ForeignKey('Address', null=True, blank=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField('Group', null=True, blank=True)

    def __str__(self):
        return f'{self.name}{" " + self.surname if self.surname else ""}'


class Address(models.Model):
    town = models.CharField(max_length=64)
    street = models.CharField(max_length=64, null=True, blank=True)
    house_no = models.CharField(max_length=8, null=True, blank=True)
    apartment_no = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f'{self.town}{", " + self.street if self.street else ""} ' \
               f'{" " + self.house_no if self.house_no else ""}' \
               f'{"/" + self.apartment_no if self.apartment_no else ""}'

    class Meta:
        unique_together = (('town', 'street', 'house_no', 'apartment_no'),)


class Phone(models.Model):

    PHONE_TYPES = (
        (1, 'mobile'),
        (2, 'home'),
        (3, 'work'),
        (4, 'other')
    )

    number = models.IntegerField(max_length=9, unique=True)
    phone_type = models.IntegerField(choices=PHONE_TYPES, null=True, blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class Email(models.Model):

    EMAIL_TYPES = (
        (1, 'private'),
        (2, 'work'),
        (3, 'other'),
    )

    email = models.CharField(max_length=64, unique=True)
    email_type = models.IntegerField(choices=EMAIL_TYPES, null=True, blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class Group(models.Model):
    group_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.group_name
