# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-27 18:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(code='invalid_name', message='name should contain only alphabets', regex='^[a-zA-Z]*$')])),
                ('description', models.CharField(max_length=250, validators=[django.core.validators.RegexValidator(code='invalid_name', message='name should contain only alphabets', regex='^[a-zA-Z]*$')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(code='invalid_name', message='name should contain only alphabets', regex='^[a-zA-Z]*$')])),
                ('description', models.CharField(max_length=250, validators=[django.core.validators.RegexValidator(code='invalid_name', message='name should contain only alphabets', regex='^[a-zA-Z]*$')])),
                ('price', models.IntegerField(max_length=10, validators=[django.core.validators.MinValueValidator(10, message='Price should be greater than 10'), django.core.validators.MaxValueValidator(100000, message='Price should be less than 100000')])),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(code='invalid_name', message='name should contain only alphabets', regex='^[a-zA-Z]*$')])),
                ('description', models.CharField(max_length=250, validators=[django.core.validators.RegexValidator(code='invalid_name', message='name should contain only alphabets', regex='^[a-zA-Z]*$')])),
                ('price', models.IntegerField(max_length=10, validators=[django.core.validators.MinValueValidator(10, message='Price should be greater than 10'), django.core.validators.MaxValueValidator(100000, message='Price should be less than 100000')])),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='products.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
