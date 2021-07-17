from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # models.IntegerField неверный выбор для phone
    phone = models.IntegerField(verbose_name='Телефон', unique=True, blank=True, null=True)
    # last_name = models.CharField(max_length=128, unique=True, blank=True, null=True)
