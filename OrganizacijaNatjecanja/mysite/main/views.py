

from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from main.models import *



def homepage(request):
    return HttpResponse('Welcome to homepage! <strong>#samoOIRI</strong>')


class OrganizatorList(ListView):
    model = Organizator

class NatjecajList(ListView):
    model = Natjecaj

class NatjecateljList(ListView):
    model = Natjecatelj


class KontaktList(ListView):
    model = Kontakt