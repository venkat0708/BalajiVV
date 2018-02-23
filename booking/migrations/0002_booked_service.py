# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-23 16:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180219_0114'),
        ('customers', '0008_auto_20180219_0404'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booked_Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start Date')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='End Time')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(10, message='Price should be greater than 10'), django.core.validators.MaxValueValidator(100000, message='Price should be less than 100000')])),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Quantity should be greater than 0'), django.core.validators.MaxValueValidator(100000, message='Quantity should be less than 100000')])),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_booked', to='booking.Event')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_served', to='products.Service')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_served', to='customers.Vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
