# Generated by Django 3.0.1 on 2020-01-15 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payment_records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrecord',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
