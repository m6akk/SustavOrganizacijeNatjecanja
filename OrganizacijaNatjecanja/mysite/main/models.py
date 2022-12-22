from django.db import models
from django.utils import timezone



class Organizator(models.Model):
    organizator_naziv = models.CharField(max_length=50)
    organizator_OIB = models.IntegerField()

    def __str__(self):
        return self.organizator_naziv




class Natjecaj(models.Model):
    natjecaj_naziv = models.CharField(max_length=50)
    natjecaj_broj = models.IntegerField()

    natjecaj_organizator = models.ForeignKey(Organizator, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.natjecaj_naziv



class Natjecatelj(models.Model):
    natjecatelj_ime = models.CharField(max_length=25)
    natjecatelj_prezime = models.CharField(max_length=25)
    natjecatelj_OIB = models.IntegerField()

    natjecatelj_natjecaji = models.ManyToManyField(Natjecaj)


    def __str__(self):
        return self.natjecatelj_ime



class Kontakt(models.Model):
    kontakt_natjecatelj_email = models.CharField(max_length=50)
    kontakt_natjecatelj_mobitel = models.CharField(max_length=50)

    kontakt_natjecatelj = models.OneToOneField(
        Natjecatelj,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.kontakt_natjecatelj_mobitel