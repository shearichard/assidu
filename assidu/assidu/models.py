from django.db import models
from datetime import date
from django.utils import timezone
from accounts.models import User
from .model_static_data import COUNTRY_ISO_CODES


class Task(models.Model):
    '''
    Represents something which the user wishes to do, typically
    every day, but possibly less frequently, say every seven days
    '''
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=255)
    startdate = models.DateField(default=date.today)
    enddate = models.DateField(blank=True, null=True)
    interval_days = models.IntegerField(default=1)


class Accomplishment(models.Model):
    '''
    Represents a time when the user accomplished a given task
    '''
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.CharField(max_length=255, blank=True)



class Country(models.Model):
    '''
    Represents a Country.

    NB: This model will only exist for a short time while
    some aspects of pytest are sorted out
    '''

    COUNTRIES = COUNTRY_ISO_CODES

    country_iso_code = models.CharField(max_length=3, choices = COUNTRIES)
    population = models.IntegerField()
    area_sq_km = models.IntegerField()


    class Meta:
        verbose_name_plural = "Countries"


    def __str__(self):
        return self.country_iso_code


class City(models.Model):
    '''
    Represents a City.

    NB: This model will only exist for a short time while
    some aspects of pytest are sorted out
    '''
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=255)
    mayor_name = models.CharField(max_length=255)
    date_of_last_mayoral_election = models.DateField()
    population = models.IntegerField()
    area_sq_km = models.IntegerField()
    elevation_metres = models.IntegerField()

    class Meta:
        verbose_name_plural = "Cities"


    def __str__(self):
        return f"{self.city_name} ({self.country.country_iso_code})"

