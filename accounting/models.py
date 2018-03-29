
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator,MaxValueValidator
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


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

    class Meta:
        unique_together = ("staff", "service")

        
    def __str__(self):
        return str(self.staff.name)+ '  '+ str(self.service.name)

    def get_absolute_url(self):
        return reverse('accounting:Commission_Structure_Detail', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('accounting:Commission_Structure_Update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('accounting:Commission_Structure_Delete', kwargs={'pk': self.id})


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

class PayCommissionOrSalary(BaseEntity):
    """ Payout to all staff members"""
    MODE_CHOICES=(
        ('BANK', 'Bank'),
        ('CHEQUE', 'Cheque'),
        ('DD', 'Demand Draft'),
        ('CASH', 'Cash'),
    )
    staff = models.ForeignKey(
            Staff,
            related_name= 'commissions_payouts'
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
        return reverse('accounting:PayCommissionOrSalary_Detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('accounting:PayCommissionOrSalary_Update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('accounting:PayCommissionOrSalary_Delete', kwargs={'id': self.id})

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
    paid_date = models.DateField(
            verbose_name='date payment is expected',
            blank =True,
            null = True,

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

    def get_absolute_url(self):
        return reverse('accounting:Invoice_Detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('accounting:Invoice_Update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('accounting:Invoice_Delete', kwargs={'id': self.id})

class Bill(BaseEntity):
    """ Invoices are generated based on events state"""

    STATUS_CHOICES=(
        ('CREATED', 'Created'),
        ('CONFIRMED', 'Confirmed'),
        ('PARTIAL_PAYMENT', 'Partially Paid'),
        ('PAID', 'Paid'),
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
            verbose_name='date bill generated'
        )
    due_date = models.DateField(
            verbose_name='date payout is expected'

        )
    paid_date = models.DateField(
            verbose_name='date payout is made',
            null = True,
            blank = True,

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
                    0,
                    message = 'Amount should be greater than 0'
                ),

                MaxValueValidator(
                    10000000,
                    message = 'Amount should be less than 10000000'
                ),
            ]
        )
    payouts = models.ManyToManyField(
            Payout,
            related_name='billed_Payouts',
            null = True,
            blank = True,
        )

    @property
    def due_amount(self):
        return self.amount - self.paid

    def get_absolute_url(self):
        return reverse('accounting:Bill_Detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('accounting:Bill_Update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('accounting:Bill_Delete', kwargs={'id': self.id})

class Commission(BaseEntity):
    """ Commissions are generated based on events state"""

    STATUS_CHOICES=(
        ('CREATED', 'Created'),
        ('CONFIRMED', 'Confirmed'),
        ('PARTIAL_PAYMENT', 'Partially Paid'),
        ('PAID', 'paid fully'),
        ('CLOSED', 'Closed')
    )
    staff = models.ForeignKey(
            Staff,
            related_name='staff_commissions',
        )
    event = models.ForeignKey(
            'booking.Event',
            related_name='event_commissions',
            blank = True,
            null =True,
        )
    booked_service = models.ForeignKey(
            'booking.Booked_Service',
            related_name='commissions',
        )
    generated_date = models.DateField(
            verbose_name='date commission generated'
        )
    due_date = models.DateField(
            verbose_name='date commission is expected'

        )
    paid_date = models.DateField(
            verbose_name='date commission is paid',
            null = True,
            blank =True

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


    def get_absolute_url(self):
        return reverse('accounting:Commission_Detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('accounting:Commission_Update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('accounting:Commission_Delete', kwargs={'id': self.id})


class Payin(BaseEntity):
    """ Payins from all customers"""
    MODE_CHOICES=(
        ('BANK', 'Bank'),
        ('CHEQUE', 'Cheque'),
        ('DD', 'Demand Draft'),
        ('CASH', 'Cash'),
    )
    customer = models.ForeignKey(
            'customers.Customer',
            related_name='customer_payins',
            blank = True,
            null = True,
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
        return reverse('accounting:Payin_Detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('accounting:Payin_Update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('accounting:Payin_Delete', kwargs={'id': self.id})


@receiver(post_save, sender = PayCommissionOrSalary)
def update_commissions_salaries_based_on_PayCommissionOrSalary_post_save(sender, instance, created, **kwargs):
    payout = instance
    amount = payout.amount
    if created:
        commissions = Commission.objects.filter(staff = payout.staff).order_by('generated_date')
        for commission in commissions:
            if amount >= commission.amount:
                commission.paid = commission.amount
                commission.status = 'PAID'
                amount -= commission.amount
                commission.save()
            elif amount > 0:
                commission.paid = amount
                commission.status = 'PARTIAL_PAYMENT'
                amount -= commission.paid
                commission.save()
