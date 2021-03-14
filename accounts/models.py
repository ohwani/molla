# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     pass

from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models. CharField(max_length=1000, null=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
