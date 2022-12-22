

from django.urls import path
from . import views
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('organizatori/', OrganizatorList.as_view()),
    path('natjecaji/', NatjecajList.as_view()),
    path('natjecatelji/', NatjecateljList.as_view()),
    path('kontakti/', KontaktList.as_view()),


]