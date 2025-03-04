from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render

from neapolitan.views import CRUDView
from .models import Country
from .forms import CountryForm

class CountryView(CRUDView):
    # The model is the only attribute that Neapolitan requires.
    model = Country

    # The form_class isn't required, but we define our own 
    # custom `CountryForm` because we
    # want more control over the widget styling.
    form_class = CountryForm

    # Controls which attributes of the model are shown in CRUD views.
    fields = ["country_iso_code", "population", "area_sq_km"]

