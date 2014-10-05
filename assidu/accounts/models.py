from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from timezone_field import TimeZoneField

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(
            email=email,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    chosen_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)
    timezone = TimeZoneField(default="Pacific/Auckland")

    objects = UserManager()
