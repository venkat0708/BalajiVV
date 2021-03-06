# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-09 20:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20170601_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(code='invalid_city', message='city should contain only alphabets', regex='^[a-zA-Z\\s]*$')]),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='city',
            field=models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(code='invalid_city', message='city should contain only alphabets', regex='^[a-zA-Z\\s]*$')]),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(code='invalid_name', message='name should contain only alphabets', regex='^[a-zA-Z\\s]*$')]),
        ),
    ]
