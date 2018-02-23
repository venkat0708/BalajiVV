from datetime import date

from django.db import models
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator, MinValueValidator,MaxValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

from core.models import BaseEntity
from customers.models import Customer,Vendor, Staff
from products.models import Service
from accounting.models import Invoice, Bill, Commission

class Event(BaseEntity):

    STATUS_CHOICES=(
        ('ENQUIRY', 'Enquiry'),
        ('CONFIRMED', 'Confirmed'),
        ('ASSIGNED', 'Assigned'),
        ('INPROGRESS', 'Inprogress'),
        ('COMPLETED', 'Completed')
    )

    customer = models.ForeignKey(
        Customer,
        related_name='events',
        blank = True,
        null = True
    )
    venue = models.CharField(
		max_length=80,
        blank=True,
        null=True,
		validators=[
			RegexValidator(
            	regex='^[0-9a-zA-Z\s]*$',
             	message='venue should contain only alphabets and numbers',
				code='invalid_name'
			),
		]
	)
    city = models.CharField(
		max_length=80,
        blank=True,
        null=True,
		validators=[
			RegexValidator(
            	regex='^[a-zA-Z\s]*$',
             	message='city should contain only alphabets',
				code='invalid_city'
			),
		]
	)
    start_date = models.DateField(
        verbose_name='Start Date',
         blank=True,
         null=True,
        )
    start_time = models.TimeField(
        verbose_name='Start Time',
    )
    end_date = models.DateField(
        verbose_name='End Date',
         blank=True,
         null=True,
        )
    end_time = models.TimeField(
        verbose_name='End Time',
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length =15,
        choices = STATUS_CHOICES,
        default = 'ENQUIRY',
    )

    def __str__(self):
        return str(self.customer) + '  ' + str(self.venue) + '  ' + str(self.city)

    def get_absolute_url(self):
        return reverse('booking:Event_Detail', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('booking:Event_Update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('booking:Event_Delete', kwargs={'pk': self.id})


class Booked_Service(BaseEntity):
    """ services of an event"""

    event = models.ForeignKey(
            Event,
            related_name='services_booked',
            on_delete=models.CASCADE
        )
    service = models.ForeignKey(
            Service,
            related_name='services_served',
            on_delete=models.CASCADE
        )
    start_date = models.DateField(
        verbose_name='Start Date',
         blank=True,
         null=True,
        )
    start_time = models.TimeField(
        verbose_name='Start Time',
    )
    end_date = models.DateField(
        verbose_name='End Date',
         blank=True,
         null=True,
        )
    end_time = models.TimeField(
        verbose_name='End Time',
        blank=True,
        null=True,
    )
    price = models.IntegerField(
        validators=[
            MinValueValidator(
                10,
                message = 'Price should be greater than 10'
            ),

            MaxValueValidator(
                100000,
                message = 'Price should be less than 100000'
            ),
        ]
    )
    quantity = models.IntegerField(
        validators=[
            MinValueValidator(
                0,
                message = 'Quantity should be greater than 0'
            ),

            MaxValueValidator(
                100000,
                message = 'Quantity should be less than 100000'
            ),
        ]
    )
    staff = models.ManyToManyField(
            Staff,
            related_name='services_assigned',
            symmetrical=False,
        )
    vendor = models.ForeignKey(
            Vendor,
            related_name='services_served',
            on_delete=models.CASCADE,
            blank = True,
            null = True,
        )
    def __str__(self):
        return self.event.__str__()

    def get_absolute_url(self):
        return reverse('booking:Booked_Service_Detail', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('booking:Booked_Service_Update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('booking:Booked_Service_Delete', kwargs={'pk': self.id})


#signals

@receiver(post_save, sender=Event)
def generate_or_modify_invoice_and_bills_based_on_event_state(sender, **kwargs):
    event = kwargs.get('instance')
    booked_services = event.services_booked.all()
    if event.status == 'COMPLETED':
        amount = 0
        for b in booked_services:
            amount += b.quantity * b.price
        try:
            invoice = Invoice.objects.get(event = event.id)
            invoice.event = event
            invoice.customer = event.customer
            invoice.amount = amount
            invoice.generated_date = timezone.now().date()
            invoice.due_date = timezone.now().date()
        except:
            invoice = Invoice(
                    event = event,
                    customer = event.customer,
                    amount= amount,
                    generated_date = timezone.now().date(),
                    paid = 0,
                    due_date = timezone.now().date(),

                )
            invoice.save()
        for b in booked_services:
            for s in b.staff.all():
                try:
                    commission = Commission.objects.get(staff = s.id)
                    commission.booked_service = b
                    commission.generated_date = timezone.now().date()
                    commission.due_date = timezone.now().date()
                    commission.amount = 500
                    commission.save()
                except:
                    commission = Commission(
                            staff = s,
                            booked_service = b,
                            amount = 500,
                            generated_date = timezone.now().date(),
                            paid = 0,
                            due_date = timezone.now().date(),
                        )
                    commission.save()
            try:
                bill = Bill.objects.get(booked_service = b.id)
                bill.vendor = b.vendor
                bill.generated_date = timezone.now().date()
                bill.due_date = timezone.now().date()
                bill.amount = b.price * b.quantity
                bill.save()
            except:
                if b.vendor:
                    bill = Bill(
                            booked_service = b,
                            vendor = b.vendor,
                            generated_date = timezone.now().date(),
                            paid = 0,
                            due_date = timezone.now().date(),
                            amount = b.price * b.quantity,
                        )
                    bill.save()
    else:
        try:
            invoice = Invoice.objects.get(event = event.id)
            invoice.delete()
        except:
            pass
        for b in booked_services:
            for s in b.staff.all():
                try:
                    commission = Commission.objects.get(staff = s.id)
                    commission.delete()
                except:
                    pass
            try:
                bill = Bill.objects.get(booked_service = b.id)
                bill.delete()
            except:
                pass
