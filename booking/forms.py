from django import forms
from django.db.models import Q

from crispy_forms.helper import FormHelper

from .models import Booked_Service, Event


class DateInput(forms.DateInput):
	input_type = 'date'


class Booked_Service_Form(forms.ModelForm):
	"""docstring for CustomerForm"""

	helper = FormHelper()
	helper.form_tag = False
	helper.form_style = 'inline'


	class Meta:
		model = Booked_Service
		exclude = ['']
		widgets = {
			'start_date' : DateInput(),
			'end_date' : DateInput(),
		}

	def __init__(self, *args, **kwargs):
		super(Booked_Service_Form, self).__init__(*args, **kwargs)
		self.fields['event'].queryset = Event.objects.filter(~Q(status='COMPLETED'))
