import pytest

from django.test import TestCase
from django.utils import timezone

from django.contrib.auth.models import User
from ..models import Country, City 


@pytest.mark.skip(reason="This test needs removing in the longer term")
@pytest.fixture(scope="module")
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()

@pytest.mark.skip(reason="This test needs removing in the longer term")
def test_empty(cards_db):
    assert cards_db.count() == 0

@pytest.mark.skip(reason="This test needs removing in the longer term")
@pytest.fixture(scope="session")
def valid_country():
    cntry_alb = Country.objects.create(country_iso_code='ALB', population=1000000, area_sq_km=50000)


@pytest.mark.skip(reason="This test needs removing in the longer term")
@pytest.mark.django_db
def test_Country_create():
  Country.objects.create(country_iso_code='ALB', population=1000000, area_sq_km=50000)
  assert Country.objects.count() == 1

@pytest.mark.skip(reason="This test needs removing in the longer term")
@pytest.mark.django_db
def test_City_create():
    #lst_cntry_alb = Country.objects.get(country_iso_code='ALB')
    lst_cntry_alb = Country.objects.get(country_iso_code='ALB')
    assert lst_cntry_alb.objects.count() == 1
    #
    '''
    City.objects.create(country_iso_code='ALB', population=1000000, area_sq_km=50000)
    assert Country.objects.count() == 1
    '''

# models test

class CountryTest(TestCase):

    def create_country(self, title="only a test", body="yes, this is only a test"):
        return Country.objects.create(country_iso_code='ALB', population=1000000, area_sq_km=50000)

    def test_country_creation_a(self):
        c = self.create_country()
        self.assertTrue(isinstance(c, Country))
        self.assertEqual(c.__str__(), c.country_iso_code)

    def test_country_creation_b(self):
        c = self.create_country()
        self.assertEqual(c.population, 1000000)


@pytest.mark.django_db
@pytest.fixture(scope="module")
def create_country_as_a_func(title="only a test", body="yes, this is only a test"):
    x = Country.objects.create(country_iso_code='USA', population=1000000, area_sq_km=50000)
    print(type(x))
    import pdb;pdb.set_trace()
    return x

@pytest.mark.django_db
def test_country_creation_as_a_function():
    print("X")
    print(type(create_country_as_a_func))
    print("X")
    local = create_country_as_a_func
    print(type(local))
    print("Z")
    import pdb;pdb.set_trace()
    assert local.__str__() ==  local.country_iso_code
    #assert isinstance(create_country_as_a_func, Country) == True





'''
@pytest.mark.django_db
@pytest.fixture(scope="module")
def create_whatever(title="only a test", body="yes, this is only a test"):
    return Whatever.objects.create(title=title, body=body, created_at=timezone.now())

def test_whatever_creation():
    w = self.create_whatever()
    self.assertTrue(isinstance(w, Whatever))
    self.assertEqual(w.__unicode__(), w.title)




'''





'''
@pytest.mark.django_db
@pytest.fixture(scope="module")
def create_whatever_as_a_func(title="only a test", body="yes, this is only a test"):
    x = Whatever.objects.create(country_iso_code='USA', population=1000000, area_sq_km=50000)
    print(type(x))
    import pdb;pdb.set_trace()
    return x
'''

'''
@pytest.mark.skip(reason="This test needs removing in the longer term")
def test_country_creation_as_a_function():
    import pdb;pdb.set_trace()
    print("X")
    print(type(create_country_as_a_func))
    print("X")
    local = create_country_as_a_func
    print(type(local))
    print("Z")
    #assert isinstance(create_country_as_a_func, Country) == True
    assert create_country_as_a_func.__str__() == create_country_as_a_func.country_iso_code
'''
