
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator,MaxValueValidator


from core.models import BaseEntity
from products.models import Service
from customers.models import Staff, Customer, Vendor


class Commission_Structure(BaseEntity):
    """ commission for staff based on services"""

    staff = models.ForeignKey(
            Staff,
            related_name='commissions'
        )
    service = models.ForeignKey(
            Service,
            related_name='commissions'
        )
    amount = models.IntegerField(
            default=500,
            validators=[
                MinValueValidator(
                    10,
                    message = 'Amount should be greater than 10'
                ),

                MaxValueValidator(
                    100000,
                    message = 'Amount should be less than 100000'
                ),
            ]
        )
    def __str__(self):
        return str(self.staff.name)+ '  '+ str(self.service.name)

    def get_absolute_url(self):
        return reverse('accounting:Commission_Structure_Detail', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('accounting:Commission_Structure_Update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('accounting:Commission_Structure_Delete', kwargs={'pk': self.id})

class Payin(BaseEntity):
    """ Payins from all customers"""
    MODE_CHOICES=(
        ('BANK', 'Bank'),
        ('CHEQUE', 'Cheque'),
        ('DD', 'Demand Draft'),
        ('CASH', 'Cash'),
    )
    event = models.ForeignKey(
            'booking.Event',
            related_name='event_payins',
            blank = True,
            null =True,
        )
    date = models.DateField(
            verbose_name='payment date'
        )
    time = models.TimeField(
            verbose_name='payment time'

        )
    amount = models.IntegerField(
            default=500,
            validators=[
                MinValueValidator(
                    10,
                    message = 'Amount should be greater than 10'
                ),

                MaxValueValidator(
                    10000000,
                    message = 'Amount should be less than 10000000'
                ),
            ]
        )
    mode = models.CharField(
        max_length =15,
        choices = MODE_CHOICES,
        default = 'CASH',
    )

    def get_absolute_url(self):
        return reverse('accounting:Payin_Detail', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('accounting:Payin_Update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('accounting:Payin_Delete', kwargs={'pk': self.id})

class Payout(BaseEntity):
    """ Payout to all vendors"""
    MODE_CHOICES=(
        ('BANK', 'Bank'),
        ('CHEQUE', 'Cheque'),
        ('DD', 'Demand Draft'),
        ('CASH', 'Cash'),
    )
    date = models.DateField(
            verbose_name='payment date'
        )
    time = models.TimeField(
            verbose_name='payment time'

        )
    amount = models.IntegerField(
            default=500,
            validators=[
                MinValueValidator(
                    10,
                    message = 'Amount should be greater than 10'
                ),

                MaxValueValidator(
                    10000000,
                    message = 'Amount should be less than 10000000'
                ),
            ]
        )
    mode = models.CharField(
        max_length =15,
        choices = MODE_CHOICES,
        default = 'CASH',
    )

    def get_absolute_url(self):
        return reverse('accounting:Payout_Detail', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('accounting:Payout_Update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('accounting:Payout_Delete', kwargs={'pk': self.id})

class Invoice(BaseEntity):
    """ Invoices are generated based on events state"""

    STATUS_CHOICES=(
        ('CREATED', 'Created'),
        ('CONFIRMED', 'Confirmed'),
        ('PARTIAL_PAYMENT', 'Partially Paid'),
        ('RECEIVED', 'Received'),
        ('CLOSED', 'Closed')
    )
    customer = models.ForeignKey(
            Customer,
            related_name='invoices',
        )
    event = models.ForeignKey(
            'booking.Event',
            related_name='invoice',
        )
    generated_date = models.DateField(
            verbose_name='date invoice generated'
        )
    due_date = models.DateField(
            verbose_name='date payment is expected'

        )
    status = models.CharField(
        max_length =15,
        choices = STATUS_CHOICES,
        default = 'CREATED',
    )
    amount = models.IntegerField(
            default=500,
            validators=[
                MinValueValidator(
                    10,
                    message = 'Amount should be greater than 10'
                ),

                MaxValueValidator(
                    10000000,
                    message = 'Amount should be less than 10000000'
                ),
            ]
        )
    paid = models.IntegerField(
            default=500,
            validators=[
                MinValueValidator(
                    10,
                    message = 'Amount should be greater than 10'
                ),

                MaxValueValidator(
                    10000000,
                    message = 'Amount should be less than 10000000'
                ),
            ]
        )
    payins = models.ManyToManyField(
            Payin,
            related_name='Payins'
        )

    def get_absolute_url(self):
        return reverse('accounting:Invoice_Detail', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('accounting:Invoice_Update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('accounting:Invoice_Delete', kwargs={'pk': self.id})

class Bill(BaseEntity):
    """ Invoices are generated based on events state"""

    STATUS_CHOICES=(
        ('CREATED', 'Created'),
        ('CONFIRMED', 'Confirmed'),
        ('PARTIAL_PAYMENT', 'Partially Paid'),
        ('RECEIVED', 'Received'),
        ('CLOSED', 'Closed')
    )
    vendor = models.ForeignKey(
            Vendor,
            related_name='vendor',
        )
    booked_service = models.ForeignKey(
            'booking.Booked_Service',
            related_name='billed_services',
        )
    generated_date = models.DateField(
            verbose_name='date invoice generated'
        )
    due_date = models.DateField(
            verbose_name='date payment is expected'

        )
    status = models.CharField(
        max_length =15,
        choices = STATUS_CHOICES,
        default = 'CREATED',
    )
    amount = models.IntegerField(
            default=500,
            validators=[
                MinValueValidator(
                    10,
                    message = 'Amount should be greater than 10'
                ),

                MaxValueValidator(
                    10000000,
                    message = 'Amount should be less than 10000000'
                ),
            ]
        )
    paid = models.IntegerField(
            default=500,
            validators=[
                MinValueValidator(
                    10,
                    message = 'Amount should be greater than 10'
                ),

                MaxValueValidator(
                    10000000,
                    message = 'Amount should be less than 10000000'
                ),
            ]
        )
    payouts = models.ManyToManyField(
            Payout,
            related_name='billed_Payouts'
        )

    def get_absolute_url(self):
        return reverse('accounting:Bill_Detail', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('accounting:Bill_Update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('accounting:Bill_Delete', kwargs={'pk': self.id})

class Commission(BaseEntity):
    """ Commissions are generated based on events state"""

    STATUS_CHOICES=(
        ('CREATED', 'Created'),
        ('CONFIRMED', 'Confirmed'),
        ('PARTIAL_PAYMENT', 'Partially Paid'),
        ('RECEIVED', 'Received'),
        ('CLOSED', 'Closed')
    )
    staff = models.ForeignKey(
            Staff,
            related_name='staff_commissions',
        )
    booked_service = models.ForeignKey(
            'booking.Booked_Service',
            related_name='commissions',
        )
    generated_date = models.DateField(
            verbose_name='date invoice generated'
        )
    due_date = models.DateField(
            verbose_name='date payment is expected'

        )
    status = models.CharField(
        max_length =15,
        choices = STATUS_CHOICES,
        default = 'CREATED',
    )
    amount = models.IntegerField(
            default=500,
            validators=[
                MinValueValidator(
                    10,
                    message = 'Amount should be greater than 10'
                ),

                MaxValueValidator(
                    10000000,
                    message = 'Amount should be less than 10000000'
                ),
            ]
        )
    paid = models.IntegerField(
            default=500,
            validators=[
                MinValueValidator(
                    10,
                    message = 'Amount should be greater than 10'
                ),

                MaxValueValidator(
                    10000000,
                    message = 'Amount should be less than 10000000'
                ),
            ]
        )
    payouts = models.ManyToManyField(
            Payout,
            related_name='Payouts'
        )

    def get_absolute_url(self):
        return reverse('accounting:Commission_Detail', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('accounting:Commission_Update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('accounting:Commission_Delete', kwargs={'pk': self.id})
