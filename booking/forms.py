from django import forms

from crispy_forms.helper import FormHelper

from .models import Booked_Service

class Booked_Service_Form(forms.ModelForm):
	"""docstring for CustomerForm"""

	helper = FormHelper()
	helper.form_tag = False
	helper.form_style = 'inline'


	class Meta:
		model = Booked_Service
		exclude = ['']
