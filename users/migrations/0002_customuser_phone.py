# Generated by Django 3.2.5 on 2021-07-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(blank=True, max_length=12, null=True, unique=True, verbose_name='Телефон'),
        ),
    ]
