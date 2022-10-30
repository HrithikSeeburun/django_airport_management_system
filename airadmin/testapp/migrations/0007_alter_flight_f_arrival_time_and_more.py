# Generated by Django 4.0.1 on 2022-01-18 10:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_alter_flight_f_arrival_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='f_arrival_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 15, 47, 6, 941174)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='f_departing_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 15, 47, 6, 941174)),
        ),
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_id', models.IntegerField(default=0, unique=True)),
                ('P_status', models.CharField(default=None, max_length=10)),
                ('P_age', models.IntegerField(default=0)),
                ('P_name', models.CharField(default=None, max_length=50)),
                ('P_gender', models.CharField(default=None, max_length=5)),
                ('flight_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='testapp.airline_company')),
            ],
        ),
    ]
