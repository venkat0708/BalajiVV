# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-29 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20180224_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked_service',
            name='staff',
            field=models.ManyToManyField(blank=True, null=True, related_name='services_assigned', to='customers.Staff'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Start Time'),
        ),
    ]
