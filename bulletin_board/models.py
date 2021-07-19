from django.db import models
from users.models import CustomUser


class Rubric(models.Model):
    name = models.CharField(verbose_name='Рубрика', max_length=128, null=True)

    def __str__(self):
        return self.name


class Bboard(models.Model):
    title = models.CharField(verbose_name='Товар', max_length=50)
    content = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=9, decimal_places=2)
    published = models.DateTimeField(verbose_name='Опубликовано', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

    def __str__(self):
        return self.title
