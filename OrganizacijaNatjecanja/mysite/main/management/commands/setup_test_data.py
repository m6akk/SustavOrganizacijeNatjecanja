import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Organizator, Natjecaj, Natjecatelj, Kontakt

from main.factory import (
    OrganizatorFactory,
    NatjecajFactory,
    NatjecateljFactory,
    KontaktFactory
)


NUM_ORGANIZATORA = 3
NUM_NATJECAJA = 3
NUM_NATJECATELJA = 3
NUM_KONTAKTA = 3


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Organizator, Natjecaj, Natjecatelj, Kontakt]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_ORGANIZATORA):
            organizator = OrganizatorFactory()

        for _ in range(NUM_NATJECAJA):
            natjecaj = NatjecajFactory()
        
        for _ in range(NUM_NATJECATELJA):
            natjecatelj = NatjecajFactory()

        for _ in range(NUM_KONTAKTA):
            kontakt = KontaktFactory()