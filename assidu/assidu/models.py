from django.db import models
from datetime import date
from django.utils import timezone
from accounts.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=255)
    startdate = models.DateField(default=date.today)
    enddate = models.DateField(blank=True, null=True)
    interval_days = models.IntegerField(default=1)


class Accomplishment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.CharField(max_length=255, blank=True)
