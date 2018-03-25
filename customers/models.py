from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from core.models import BaseEntity
from Balaji.users.models import User
# Create your models here.
class Customer(BaseEntity):
	"""docstring for Customer"""

	user = models.OneToOneField(
			User,
			blank = True,
			null = True
		)
	name = models.CharField(
		max_length=80,
		validators=[
			RegexValidator(
            	regex='^[a-zA-Z\s]*$',
             	message='name should contain only alphabets',
				code='invalid_name'
			),
		]
	)
	address = models.CharField(max_length=80)
	city = models.CharField(
		max_length=80,
		validators=[
			RegexValidator(
            	regex='^[a-zA-Z\s]*$',
             	message='city should contain only alphabets',
				code='invalid_city'
			),
		]
	)
	phone_number = models.CharField(
		max_length=13,
		validators=[
        RegexValidator(
            regex='^[0-9]{10}$',
            message='Phone number should contain only 10 numbers',
			code='invalid Phone number'
			),
    	]
	)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name




class Vendor(BaseEntity):
	"""docstring for Vendor"""

	user = models.OneToOneField(
			User,
			blank = True,
			null = True
		)
	name = models.CharField(
		max_length=80,
		validators=[
			RegexValidator(
            	regex='^[a-zA-Z\s]*$',
             	message='name should contain only alphabets',
				code='invalid_name'
			),
		]
	)
	address = models.CharField(max_length=80)
	city = models.CharField(
		max_length=80,
		validators=[
			RegexValidator(
            	regex='^[a-zA-Z\s]*$',
             	message='city should contain only alphabets',
				code='invalid_city'
			),
		]
	)
	phone_number = models.CharField(
		max_length=13,
		validators=[
        RegexValidator(
            regex='^[0-9]{10}$',
            message='Phone number should contain only 10 numbers',
			code='invalid Phone number'
			),
    	]
	)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class Staff(BaseEntity):
	"""docstring for Staff"""

	user = models.OneToOneField(
			User,
			blank = True,
			null = True
		)
	name = models.CharField(
		max_length=80,
		validators=[
			RegexValidator(
            	regex='^[a-zA-Z\s]*$',
             	message='name should contain only alphabets',
				code='invalid_name'
			),
		]
	)
	address = models.CharField(max_length=80)
	city = models.CharField(
		max_length=80,
		validators=[
			RegexValidator(
            	regex='^[a-zA-Z\s]*$',
             	message='city should contain only alphabets',
				code='invalid_city'
			),
		]
	)
	phone_number = models.CharField(
		max_length=13,
		validators=[
        RegexValidator(
            regex='^[0-9]{10}$',
            message='Phone number should contain only 10 numbers',
			code='invalid Phone number'
			),
    	]
	)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('customers:Staff_Detail', kwargs={'pk': self.id})

	def get_update_url(self):
		return reverse('customers:Staff_Update', kwargs={'pk': self.id})

	def get_delete_url(self):
		return reverse('customers:Staff_Delete', kwargs={'pk': self.id})
