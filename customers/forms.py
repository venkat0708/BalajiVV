from django import forms

from crispy_forms.helper import FormHelper

from .models import Customer,Vendor

class CustomerForm(forms.ModelForm):
	"""docstring for CustomerForm"""
	
	helper = FormHelper()
	helper.form_tag = False
	helper.form_style = 'inline'
	

	class Meta:
		model = Customer
		exclude = ['user',]
		

class VendorForm(forms.ModelForm):
	"""docstring for CustomerForm"""
	
	helper = FormHelper()
	helper.form_tag = False
	helper.form_style = 'inline'


	class Meta:
		model = Vendor
		exclude = ['user',]
		