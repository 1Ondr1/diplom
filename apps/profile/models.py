from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    last_seen = models.DateTimeField(null=True, blank=True)