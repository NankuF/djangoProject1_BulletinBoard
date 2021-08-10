# Generated by Django 3.2.5 on 2021-07-28 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True, verbose_name='Рубрика')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Bboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Товар')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Цена')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('rubric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bulletin_board.rubric', verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-published'],
            },
        ),
    ]