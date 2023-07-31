from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email Address")
    username = models.CharField(max_length=255, unique=True, verbose_name="Username")
    phone_number = models.CharField(max_length=12, verbose_name="Phone Number")
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    profile_picture = models.ImageField(upload_to='accounts/', default='accounts/default.png')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone_number", "first_name", "last_name"]