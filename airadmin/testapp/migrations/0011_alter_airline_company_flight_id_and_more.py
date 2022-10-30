# Generated by Django 4.0.1 on 2022-02-06 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0010_store_alter_flight_f_arrival_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline_company',
            name='flight_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='flight',
            name='f_arrival_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 23, 40, 24, 440013)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='f_departing_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 23, 40, 24, 440013)),
        ),
        migrations.AlterField(
            model_name='runway',
            name='lock_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 23, 40, 24, 440013)),
        ),
        migrations.AlterField(
            model_name='runway',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 23, 40, 24, 440013)),
        ),
    ]
