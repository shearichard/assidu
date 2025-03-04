import hashlib
import datetime
import pytest
#
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
#
from assidu.models import Country, City 


def make_random_string(maxlngth=20):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%Y%m%d%H%M%S%f')
    # Encrypt the date time using a hashing algorithm
    hash_object = hashlib.sha256(formatted_datetime.encode())
    random_hash = hash_object.hexdigest()
    #
    return random_hash[:maxlngth]


def make_random_username():
    uid_suffix = make_random_string()
    return "uid-" + uid_suffix


def make_random_password():
    uid_suffix = make_random_string()
    return "pwd-" + uid_suffix


@pytest.fixture(scope="session")
def unauthenticated_api_client():
    return APIClient()


'''
@pytest.fixture()
def neo_using_organisation(neo_using_organisation_name):
    # Create a NEO Using Organisation
    org = NeoUsingOrganisation(name=neo_using_organisation_name)
    org.save()
    return org
'''


'''
@pytest.fixture()
def authenticated_api_client():
    # Create a user for authentication
    user = User.objects.create_user(username=make_random_username(), password=make_random_password())
    # Generate a token for the user
    token, _ = Token.objects.get_or_create(user=user)
    # Add the Authorization header to the client
    api_client = APIClient()
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return api_client
'''


@pytest.fixture()
def create_country(cntry_iso_cde="DEU", popultn=100, areasqkm=101):
    c = Country.objects.create(country_iso_code=cntry_iso_cde, population=popultn, area_sq_km=areasqkm)
    return c

@pytest.fixture
def username():
	#Temporary only https://docs.pytest.org/en/latest/how-to/fixtures.html#override-a-fixture-with-direct-test-parametrization
	return 'username'

@pytest.fixture
def other_username(username):
	#Temporary only https://docs.pytest.org/en/latest/how-to/fixtures.html#override-a-fixture-with-direct-test-parametrization
	return 'other-' + username
