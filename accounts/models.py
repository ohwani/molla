from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    last_name = None
    first_name = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    name = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=200)
    phone = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null= True)

    def __str__(self):
        return self.email