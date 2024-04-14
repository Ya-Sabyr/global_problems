from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default=None)
    last_name = models.CharField(max_length=30, default=None)
    bio = models.TextField(blank=True)