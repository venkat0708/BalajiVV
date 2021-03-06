# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-23 20:24
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0009_staff'),
        ('products', '0004_auto_20180219_0114'),
        ('booking', '0005_auto_20180224_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('generated_date', models.DateField(verbose_name='date invoice generated')),
                ('due_date', models.DateField(verbose_name='date payment is expected')),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('CONFIRMED', 'Confirmed'), ('PARTIAL_PAYMENT', 'Partially Paid'), ('RECEIVED', 'Received'), ('CLOSED', 'Closed')], default='CREATED', max_length=15)),
                ('amount', models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(10, message='Amount should be greater than 10'), django.core.validators.MaxValueValidator(10000000, message='Amount should be less than 10000000')])),
                ('paid', models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(10, message='Amount should be greater than 10'), django.core.validators.MaxValueValidator(10000000, message='Amount should be less than 10000000')])),
                ('booked_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billed_services', to='booking.Booked_Service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('generated_date', models.DateField(verbose_name='date invoice generated')),
                ('due_date', models.DateField(verbose_name='date payment is expected')),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('CONFIRMED', 'Confirmed'), ('PARTIAL_PAYMENT', 'Partially Paid'), ('RECEIVED', 'Received'), ('CLOSED', 'Closed')], default='CREATED', max_length=15)),
                ('amount', models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(10, message='Amount should be greater than 10'), django.core.validators.MaxValueValidator(10000000, message='Amount should be less than 10000000')])),
                ('paid', models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(10, message='Amount should be greater than 10'), django.core.validators.MaxValueValidator(10000000, message='Amount should be less than 10000000')])),
                ('booked_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commissions', to='booking.Booked_Service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Commission_Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(10, message='Amount should be greater than 10'), django.core.validators.MaxValueValidator(100000, message='Amount should be less than 100000')])),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commissions', to='products.Service')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commissions', to='customers.Staff')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('generated_date', models.DateField(verbose_name='date invoice generated')),
                ('due_date', models.DateField(verbose_name='date payment is expected')),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('CONFIRMED', 'Confirmed'), ('PARTIAL_PAYMENT', 'Partially Paid'), ('RECEIVED', 'Received'), ('CLOSED', 'Closed')], default='CREATED', max_length=15)),
                ('amount', models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(10, message='Amount should be greater than 10'), django.core.validators.MaxValueValidator(10000000, message='Amount should be less than 10000000')])),
                ('paid', models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(10, message='Amount should be greater than 10'), django.core.validators.MaxValueValidator(10000000, message='Amount should be less than 10000000')])),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='customers.Customer')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='booking.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(verbose_name='payment date')),
                ('time', models.TimeField(verbose_name='payment time')),
                ('amount', models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(10, message='Amount should be greater than 10'), django.core.validators.MaxValueValidator(10000000, message='Amount should be less than 10000000')])),
                ('mode', models.CharField(choices=[('BANK', 'Bank'), ('CHEQUE', 'Cheque'), ('DD', 'Demand Draft'), ('CASH', 'Cash')], default='CASH', max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(verbose_name='payment date')),
                ('time', models.TimeField(verbose_name='payment time')),
                ('amount', models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(10, message='Amount should be greater than 10'), django.core.validators.MaxValueValidator(10000000, message='Amount should be less than 10000000')])),
                ('mode', models.CharField(choices=[('BANK', 'Bank'), ('CHEQUE', 'Cheque'), ('DD', 'Demand Draft'), ('CASH', 'Cash')], default='CASH', max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='payins',
            field=models.ManyToManyField(related_name='Payins', to='accounting.Payin'),
        ),
        migrations.AddField(
            model_name='commission',
            name='payouts',
            field=models.ManyToManyField(related_name='Payouts', to='accounting.Payout'),
        ),
        migrations.AddField(
            model_name='commission',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_commissions', to='customers.Staff'),
        ),
        migrations.AddField(
            model_name='bill',
            name='payouts',
            field=models.ManyToManyField(related_name='billed_Payouts', to='accounting.Payout'),
        ),
        migrations.AddField(
            model_name='bill',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to='customers.Vendor'),
        ),
    ]
