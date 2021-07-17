from django.db import models
from users.models import CustomUser


class Bboard(models.Model):
    title = models.CharField(verbose_name='Товар', max_length=50)
    content = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=9, decimal_places=2)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)  # ???

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
