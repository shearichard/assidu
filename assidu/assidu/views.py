from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Experiment with fbv START
from django.template.response import TemplateResponse
# Experiment with fbv END
# Experiment with CBBV START
#from django.views.generic.list import ListView
# Experiment with CBBV END


from neapolitan.views import CRUDView
from .models import Country, City
from .forms import CountryForm, CityForm

class CountryView(CRUDView):
    # The model is the only attribute that Neapolitan requires.
    model = Country

    # The form_class isn't required, but we define our own 
    # custom `CountryForm` because we
    # want more control over the widget styling.
    form_class = CountryForm

    # Controls which attributes of the model are shown in CRUD views.
    fields = ["country_iso_code", "population", "area_sq_km"]


class CityView(CRUDView):
    # The model is the only attribute that Neapolitan requires.
    model = City 

    # The form_class isn't required, but we define our own 
    # custom `CountryForm` because we
    # want more control over the widget styling.
    form_class = CityForm

    # Controls which attributes of the model are shown in CRUD views.
    fields = [ "country", "city_name", "mayor_name", "date_of_last_mayoral_election", "population", "area_sq_km", "elevation_metres", "some_number"]


def city_list(request):
    header_list = ['id', 'name']
    city_list = []
    city_list.append({'id':1,'name':'Paris'})
    city_list.append({'id':2,'name':'London'})
    city_list.append({'id':3,'name':'Rome'})
    #
    template_context = {}
    template_context['create_view_url'] = 'foo'
    template_context['object_verbose_name'] = 'City'
    template_context['object_list'] = city_list
    template_context['header_list'] = header_list
    #
    return TemplateResponse(request, 'assidu/city_list.html', template_context) 

