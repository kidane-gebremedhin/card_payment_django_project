# Generated by Django 3.0.1 on 2020-01-15 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20200102_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=None, editable=False, null=True),
        ),
    ]
