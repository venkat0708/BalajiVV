# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-23 17:01
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0008_auto_20180219_0404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(code='invalid_name', message='name should contain only alphabets', regex='^[a-zA-Z\\s]*$')])),
                ('address', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator(code='invalid_city', message='city should contain only alphabets', regex='^[a-zA-Z\\s]*$')])),
                ('phone_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(code='invalid Phone number', message='Phone number should contain only 10 numbers', regex='^[0-9]{10}$')])),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
