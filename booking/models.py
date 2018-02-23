from datetime import date

from django.db import models
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator, MinValueValidator,MaxValueValidator

from core.models import BaseEntity
from customers.models import Customer,Vendor, Staff
from products.models import Service

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
