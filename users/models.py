from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    # last_name = models.CharField(max_length=128, unique=True, blank=True, null=True)
