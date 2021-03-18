# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     pass

from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth.models import User

from .regex import EMAIL_RegEx, Message
import re


class User(models.Model):
    email = models.EmailField()
    password = models. CharField(max_length=1000, null=True)
    password2 = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'

class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F','Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True)
    name = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=240, blank=True)
    gender = models.CharField(max_length=1, choices = GENDER_CHOICES, null=True)
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    ratings = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user

        class Meta:
            db_table = 'reviews'
