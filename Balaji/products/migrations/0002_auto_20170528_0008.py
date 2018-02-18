# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-27 18:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True, validators=[django.core.validators.RegexValidator(code='invalid_name', message='name should contain only alphabets', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10, message='Price should be greater than 10'), django.core.validators.MaxValueValidator(100000, message='Price should be less than 100000')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True, validators=[django.core.validators.RegexValidator(code='invalid_name', message='name should contain only alphabets', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10, message='Price should be greater than 10'), django.core.validators.MaxValueValidator(100000, message='Price should be less than 100000')]),
        ),
    ]