from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models


from Balaji.users.models import User
# Create your models here.
class Customer(models.Model):
	"""docstring for Customer"""
	
	user = models.OneToOneField(
			User,
			blank = True,
			null = True
		)
	name = models.CharField(max_length=80)
	address = models.CharField(max_length=80)
	city = models.CharField(max_length=80)
	phone_number = models.CharField(max_length=13)

	def __str__(self):
		return self.name


class Vendor(models.Model):
	"""docstring for Customer"""
	
	user = models.OneToOneField(
			User,
			blank = True,
			null = True
		)
	name = models.CharField(max_length=80)
	address = models.CharField(max_length=80)
	city = models.CharField(max_length=80)
	phone_number = models.CharField(max_length=13)

	def __str__(self):
		return self.name

		