from django.test import TestCase
from assidu.models import Country, City 
from django.utils import timezone

# models test
class CountryTest(TestCase):

    def create_city(self, cntry_iso_cde="DEU", popultn=100, areasqkm=101):
        return Country.objects.create(country_iso_code=cntry_iso_cde, population=popultn, area_sq_km=areasqkm)

    def test_city_creation(self):
        c = self.create_city()
        self.assertTrue(isinstance(c, Country))
        self.assertEqual(c.__str__(), c.country_iso_code)
