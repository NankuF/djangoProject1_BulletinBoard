# Generated by Django 3.2.5 on 2021-07-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0002_bboard_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bboard',
            options={'ordering': ['-published'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterField(
            model_name='bboard',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано'),
        ),
    ]