# Generated by Django 3.2.5 on 2021-07-18 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0004_auto_20210718_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True, verbose_name='Рубрика')),
            ],
        ),
        migrations.AddField(
            model_name='bboard',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bulletin_board.rubric'),
        ),
    ]