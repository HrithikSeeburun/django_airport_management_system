# Generated by Django 4.0.1 on 2022-02-28 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0015_alter_runway_lock_time_alter_runway_release_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runway',
            name='lock_time',
            field=models.TimeField(default=datetime.datetime(2022, 2, 28, 12, 59, 33, 723285)),
        ),
        migrations.AlterField(
            model_name='runway',
            name='release_time',
            field=models.TimeField(default=datetime.datetime(2022, 2, 28, 12, 59, 33, 723285)),
        ),
    ]
