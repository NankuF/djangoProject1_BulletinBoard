from django.db import models

# from django.urls import reverse
# from django.utils.text import slugify

from users.models import CustomUser


class Rubric(models.Model):
    name = models.CharField(verbose_name='Рубрика', max_length=128, null=True)
    slug = models.SlugField(verbose_name='URL', max_length=128, unique=True)

    def __str__(self):
        return self.name

    # не пригодилось
    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse('current_rubric', kwargs={'rubric_slug': self.slug})

    # не пригодилось
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super(Rubric, self).save(*args, **kwargs)


class Bboard(models.Model):
    title = models.CharField(verbose_name='Товар', max_length=50)
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True)
    content = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=9, decimal_places=0)
    published = models.DateTimeField(verbose_name='Опубликовано', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, null=True, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

    def __str__(self):
        return self.title

    # не пригодилось
    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse('bboard:by_rubric', kwargs={'rubric_slug': self.slug})
