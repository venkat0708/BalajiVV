# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-24 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0005_auto_20180324_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='paid_date',
            field=models.DateField(blank=True, null=True, verbose_name='date commission is paid'),
        ),
    ]
