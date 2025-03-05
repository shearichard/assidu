import pprint
#
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
#
from assidu.models import Country, City 
from assidu.forms import CountryForm 

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

    # Test views
    def test_valid_form(self):
        c = Country.objects.create(country_iso_code="USA", population=200, area_sq_km=201)
        print("Test valid form A0")
        print(c.country_iso_code)
        print(c.population)
        print(c.area_sq_km)
        print("Test valid form A1")
        data = { "country_iso_code": "Angola" , "population": c.population , "area_sq_km": c.area_sq_km }
        data = { "id_country_iso_code": c.country_iso_code, "id_population": c.population , "id_area_sq_km": c.area_sq_km }
        data = { "country_iso_code": c.country_iso_code, "population": c.population , "area_sq_km": c.area_sq_km }
        data = { "id_country_iso_code": "Angola" , "id_population": c.population , "id_area_sq_km": c.area_sq_km }
        data = { "country_iso_code": "Angola" , "population": c.population , "area_sq_km": c.area_sq_km }
        data = { "country_iso_code": c.country_iso_code, "population": c.population , "area_sq_km": c.area_sq_km }
        import pdb;pdb.set_trace()
        form = CountryForm(data)
        #
        print("Test valid form A1-1")
        if form.is_valid():
            pass
        else:
            pprint.pprint(form.errors)
        #
        print("Test valid form A1-2")
        if False:
            print(form.as_div())
            print("Test valid form A2")
            pprint.pprint(dir(form))
            print("Test valid form B0")
            err_dict = form.errors.as_data()
            print("Test valid form B1")
            for k, v in err_dict:
                print(k, " -> ", v)
            print("Test valid form B2")
            pprint.pprint(dir(err_dict))
            print("Test valid form C")
            #print(form.non_field_errors())
            print("Test valid form D")
            print(type(form.is_valid()))
            print("Test valid form E")
        #
        self.assertTrue(form.is_valid())

    '''
    def test_invalid_form(self):
        c = Country.objects.create(country_iso_code="BBB", population=200, area_sq_km=201)
        data = { }
        form = CountryForm(data=data)
        self.assertFalse(form.is_valid())
    '''
