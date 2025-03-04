from django import forms
from .models import Country

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country 
        fields = ["country_iso_code", "population", "area_sq_km"]
