# Generated by Django 3.0.1 on 2020-01-18 10:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20200115_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
