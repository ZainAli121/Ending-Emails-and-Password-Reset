from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=200, null=True, unique=True)
    password = models.CharField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.username