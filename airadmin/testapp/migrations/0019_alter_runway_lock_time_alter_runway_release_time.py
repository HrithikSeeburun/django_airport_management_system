# Generated by Django 4.0.1 on 2022-02-28 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0018_remove_flight_f_arrival_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runway',
            name='lock_time',
            field=models.TimeField(default=datetime.datetime(2022, 2, 28, 15, 9, 16, 752455)),
        ),
        migrations.AlterField(
            model_name='runway',
            name='release_time',
            field=models.TimeField(default=datetime.datetime(2022, 2, 28, 15, 9, 16, 752455)),
        ),
    ]
