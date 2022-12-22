


from django.contrib import admin
from . models import *

model_list = [Organizator, Natjecaj, Natjecatelj, Kontakt]
admin.site.register(model_list)