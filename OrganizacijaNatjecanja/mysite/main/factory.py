import factory
import random

from main.models import *

class OrganizatorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organizator

    organizator_naziv = factory.Faker('company')
    organizator_OIB = factory.Faker('random_number', digits=11)

class NatjecajFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Natjecaj

    natjecaj_naziv = factory.Faker('word')
    natjecaj_broj = factory.Faker('random_number', digits=4)
    natjecaj_organizator = factory.SubFactory(OrganizatorFactory)

class NatjecateljFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Natjecatelj

    natjecatelj_ime = factory.Faker('first_name')
    natjecatelj_prezime = factory.Faker('last_name')
    natjecatelj_OIB = factory.Faker('random_number', digits=11)


class KontaktFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Kontakt

    kontakt_natjecatelj_email = factory.Faker('email')
    kontakt_natjecatelj_mobitel = factory.Faker('phone_number')
    kontakt_natjecatelj = factory.SubFactory(NatjecateljFactory)