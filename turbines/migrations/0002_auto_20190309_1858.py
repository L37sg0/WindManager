# Generated by Django 2.1.7 on 2019-03-09 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turbines', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turbine',
            name='epro_provid',
        ),
        migrations.RemoveField(
            model_name='turbine',
            name='forecast_type',
        ),
        migrations.RemoveField(
            model_name='turbine',
            name='number_of_turbines',
        ),
        migrations.RemoveField(
            model_name='turbine',
            name='percent',
        ),
        migrations.RemoveField(
            model_name='turbine',
            name='provid_name',
        ),
        migrations.RemoveField(
            model_name='turbine',
            name='wind_plant',
        ),
    ]
