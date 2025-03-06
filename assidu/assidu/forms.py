from django import forms
from .models import Country, City

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country 
        fields = ["country_iso_code", "population", "area_sq_km"]


class CityForm(forms.ModelForm):
    class Meta:
        model = City 
        fields = ["country",
                "city_name",
                "mayor_name",
                "date_of_last_mayoral_election",
                "population",
                "area_sq_km", 
                "elevation_metres", 
                "some_number"]

