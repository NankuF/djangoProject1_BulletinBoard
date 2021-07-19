import hashlib
import random
from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class CustomUser(AbstractUser):
    # models.IntegerField неверный выбор для phone
    phone = models.CharField(verbose_name='Телефон', unique=True, max_length=12, blank=True, null=True)
    activation_key = models.CharField(max_length=128, blank=True, null=True)
    activation_key_expires = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.is_active = False

            salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
            self.activation_key = hashlib.sha1((self.email + salt).encode('utf8')).hexdigest()
            self.activation_key_expires = now() + timedelta(hours=48)

            self.email_user(
                subject='Ключ активации',
                message=f"""
                {self.username}, для активации аккаунта перейдите по ссылке 
                http://127.0.0.1:8000/{settings.APP_NAME}/activate/{self.activation_key}                 
                """,
                from_email=settings.EMAIL_HOST_USER)

        super(CustomUser, self).save(*args, **kwargs)

    def is_activation_key_expires(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True

        # def email_user(self, subject, message, from_email=None, **kwargs):
        #     """Send an email to this user."""
        #     send_mail(subject, message, from_email, [self.email], **kwargs)
