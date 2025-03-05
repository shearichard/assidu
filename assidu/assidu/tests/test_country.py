from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
#
from assidu.models import Country, City 

# models test
class CountryTest(TestCase):

    def create_city(self, cntry_iso_cde="DEU", popultn=100, areasqkm=101):
        return Country.objects.create(country_iso_code=cntry_iso_cde, population=popultn, area_sq_km=areasqkm)

    # Test model
    def test_city_creation(self):
        c = self.create_city()
        self.assertTrue(isinstance(c, Country))
        self.assertEqual(c.__str__(), c.country_iso_code)

    # Test views
    def test_country_list_view(self, cntry_iso_cde="DEU", popultn=100, areasqkm=101):
        url = reverse("country-list")
        #
        c = Country.objects.create(country_iso_code=cntry_iso_cde, population=popultn, area_sq_km=areasqkm)
        resp = self.client.get(url)
        #
        self.assertEqual(resp.status_code, 200)
        #
        self.assertIn(c.country_iso_code.encode('latin1'), resp.content)
        self.assertIn(str(c.population).encode('latin1'), resp.content)
        self.assertIn(str(c.area_sq_km).encode('latin1'), resp.content)
        self.assertNotIn(b"FRA", resp.content)
        #
        c = Country.objects.create(country_iso_code="FRA", population=200, area_sq_km=201)
        resp = self.client.get(url)
        #
        self.assertEqual(resp.status_code, 200)
        #
        self.assertIn(c.country_iso_code.encode('latin1'), resp.content)
        self.assertIn(str(c.population).encode('latin1'), resp.content)
        self.assertIn(str(c.area_sq_km).encode('latin1'), resp.content)
        self.assertIn(b"FRA", resp.content)

