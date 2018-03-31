
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator,MaxValueValidator
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete
from django.utils import timezone


from core.models import BaseEntity
from products.models import Service
from customers.models import Staff, Customer, Vendor

class CommissionStructure(BaseEntity):
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
        return reverse('customers:Staff_Detail', kwargs={'pk': self.staff.id})

    def get_update_url(self):
        return reverse('accounting:CommissionStructure_Update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('accounting:CommissionStructure_Delete', kwargs={'pk': self.id})


class Payout(BaseEntity):
    """ Payout to all vendors"""
    MODE_CHOICES=(
        ('BANK', 'Bank'),
        ('CHEQUE', 'Cheque'),
        ('DD', 'Demand Draft'),
        ('CASH', 'Cash'),
    )
    vendor = models.ForeignKey(
            Vendor,
            related_name='bill_payouts'
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

    def __str__(self):
        return self.vendor.name

    def get_absolute_url(self):
        return reverse('accounting:Payout_Detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('accounting:Payout_Update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('accounting:Payout_Delete', kwargs={'id': self.id})

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
    payins = models.ManyToManyField(
            Payin,
            related_name='invoices',
            null = True,
            blank = True,
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
            related_name='bills',
            null = True,
            blank = True,
        )

    @property
    def due_amount(self):
        return self.amount - self.paid

    def __str__(self):
        return self.vendor.name

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
            PayCommissionOrSalary,
            related_name='commissions',
            null = True,
            blank = True,
        )


    def get_absolute_url(self):
        return reverse('accounting:Commission_Detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('accounting:Commission_Update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('accounting:Commission_Delete', kwargs={'id': self.id})





@receiver(post_save, sender = PayCommissionOrSalary)
def update_commissions_salaries_based_on_PayCommissionOrSalary_post_save(sender, instance, created, **kwargs):
    payout = instance
    amount = payout.amount
    commissions = Commission.objects.filter(staff = payout.staff).order_by('generated_date')
    for commission in commissions:
        if amount >= commission.amount:
            commission.paid = commission.amount
            commission.status = 'PAID'
            amount -= commission.amount
            commission.paid_date = timezone.now().date()
            commission.payouts.add(payout)
            commission.save()
        elif amount > 0:
            commission.paid += amount
            if commission.paid < commission.amount:
                commission.status = 'PARTIAL_PAYMENT'
            else:
                commission.status = 'PAID'
                commission.paid_date = timezone.now().date()
            amount -= commission.paid
            commission.payouts.add(payout)
            commission.save()


@receiver(pre_save, sender = PayCommissionOrSalary)
def update_bill_based_on_PayCommissionOrSalary_pre_save(sender, instance, **kwargs):
    print('triggered pre save PayCommissionOrSalary')
    payout = instance
    try:
        past_payout = PayCommissionOrSalary.objects.get(pk = payout.id)
        amount = past_payout.amount
        commissions = past_payout.commissions.all()
        for commission in commissions:
            if amount >=0:
                if commission.paid < amount:
                    commission.paid = 0
                    commission.status = 'CONFIRMED'
                    commission.save()
                    commission -= commission.paid
                elif commission.paid >= amount:
                    commission.paid -= amount
                    commission.status = 'PARTIAL_PAYMENT'
                    commission.save()
                    amount -= commission.paid
    except:
        pass

@receiver(pre_delete, sender = PayCommissionOrSalary)
def update_bill_based_on_payout_pre_save(sender, instance, **kwargs):
    print('triggered pre delete PayCommissionOrSalary' )
    payout = instance
    try:
        delted_payout = PayCommissionOrSalary.objects.get(pk = payout.id)
        amount = delted_payout.amount
        commissions = delted_payout.commissions.all()
        print(commissions)
        for commission in commissions:
            if amount >0:
                if commission.paid <= amount:
                    commission.paid = 0
                    commission.status = 'CONFIRMED'
                    commission.save()
                    amount -= commission.paid
                elif commission.paid > amount:
                    commission.paid -= amount
                    commission.status = 'PARTIAL_PAYMENT'
                    commission.save()
                    amount -= commission.paid
    except:
        print('failed')




@receiver(post_save, sender = Payout)
def update_bill_based_on_payout_post_save(sender, instance, created, **kwargs):
    print('triggered post save payout')
    payout = instance
    amount = payout.amount
    bills = Bill.objects.filter(vendor = payout.vendor).order_by('generated_date')
    for bill in bills:
        if bill.paid < bill.amount:
            if amount >= bill.amount:
                bill.paid = bill.amount
                bill.status = 'PAID'
                amount -= bill.amount
                bill.paid_date = timezone.now().date()
                bill.payouts.add(payout)
                bill.save()
            elif amount > 0:
                bill.paid += amount
                if bill.paid < bill.amount:
                    bill.status = 'PARTIAL_PAYMENT'
                else:
                    bill.status = 'PAID'
                    bill.paid_date = timezone.now().date()
                amount -= bill.paid
                bill.payouts.add(payout)
                bill.save()



@receiver(pre_save, sender = Payout)
def update_bill_based_on_payout_pre_save(sender, instance, **kwargs):
    print('triggered pre save payout')
    payout = instance
    try:
        past_payout = Payout.objects.get(pk = payout.id)
        amount = past_payout.amount
        bills = past_payout.bills.all()
        for bill in bills:
            if amount >0:
                if bill.paid <= amount:
                    bill.paid = 0
                    bill.status = 'CONFIRMED'
                    bill.save()
                    amount -= bill.paid
                elif bill.paid > amount:
                    bill.paid -= amount
                    bill.status = 'PARTIAL_PAYMENT'
                    bill.save()
                    amount -= bill.paid
    except:
        pass


@receiver(pre_delete, sender = Payout)
def update_bill_based_on_payout_pre_save(sender, instance, **kwargs):
    print('triggered pre delete payout' )
    payout = instance
    try:
        delted_payout = Payout.objects.get(pk = payout.id)
        amount = delted_payout.amount
        bills = delted_payout.bills.all()
        for bill in bills:
            if amount >0:
                if bill.paid < amount:
                    bill.paid = 0
                    bill.status = 'CONFIRMED'
                    bill.save()
                    amount -= bill.paid
                elif bill.paid > amount:
                    bill.paid -= amount
                    bill.status = 'PARTIAL_PAYMENT'
                    bill.save()
                    amount -= bill.paid
    except:
        pass
