# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-24 13:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_staff'),
        ('accounting', '0003_auto_20180224_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayCommissionOrSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(verbose_name='payment date')),
                ('time', models.TimeField(verbose_name='payment time')),
                ('amount', models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(10, message='Amount should be greater than 10'), django.core.validators.MaxValueValidator(10000000, message='Amount should be less than 10000000')])),
                ('mode', models.CharField(choices=[('BANK', 'Bank'), ('CHEQUE', 'Cheque'), ('DD', 'Demand Draft'), ('CASH', 'Cash')], default='CASH', max_length=15)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commissions_payouts', to='customers.Staff')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='payin',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payins', to='accounting.Invoice'),
        ),
    ]
