# Generated by Django 2.1.7 on 2019-03-11 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turbines', '0003_remove_turbine_supported_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_date', models.DateTimeField(verbose_name='date published')),
                ('repair_type', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'повреди',
            },
        ),
        migrations.CreateModel(
            name='TechGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('techgroup_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'работни групи',
            },
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technician_name', models.CharField(max_length=20)),
                ('technician_techgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turbines.TechGroup')),
            ],
            options={
                'verbose_name_plural': 'техници',
            },
        ),
        migrations.AddField(
            model_name='repair',
            name='technician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turbines.Technician'),
        ),
        migrations.AddField(
            model_name='repair',
            name='turbine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turbines.Turbine'),
        ),
    ]
