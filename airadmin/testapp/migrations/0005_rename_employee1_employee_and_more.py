# Generated by Django 4.0.1 on 2022-01-18 10:14

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0004_alter_flight_f_arrival_time_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='employee1',
            new_name='Employee',
        ),
        migrations.AlterField(
            model_name='flight',
            name='f_arrival_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 15, 43, 57, 740112)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='f_departing_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 15, 43, 57, 740112)),
        ),
    ]
