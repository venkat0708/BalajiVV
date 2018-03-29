from django import forms
from django.db.models import Q

from crispy_forms.helper import FormHelper

from .models import Payin, PayCommissionOrSalary, Commission, Invoice, Bill
from booking.models import Event

class DateInput(forms.DateInput):
	input_type = 'date'

class PayinForm(forms.ModelForm):
    """ form for payins"""
    helper = FormHelper()
    helper.form_tag = False
    helper.form_style = 'inline'

    class Meta:
        model = Payin
        exclude = ['']
        widgets = {
			'date' : DateInput(),
		}

    def __init__(self, *args, **kwargs):
        super(PayinForm, self).__init__(*args, **kwargs)
        self.fields['event'].queryset = Event.objects.filter(~Q(invoice__status = 'PAID'))

class PayCommissionOrSalaryForm(forms.ModelForm):
    """ form for PayCommissionOrSalary """

    helper = FormHelper()
    helper.form_tag = False
    helper.form_style = 'inline'

    class Meta:
        model = PayCommissionOrSalary
        exclude = ['']
        widgets = {
			'date' : DateInput(),
		}


class CommissionForm(forms.ModelForm):
	"""Form for Commission"""

	helper = FormHelper()
	helper.form_tag = False
	helper.form_style = 'inline'

	class Meta:
		model = Commission
		exclude =['']
		widgets = {
			'generated_date':DateInput(),
			'due_date':DateInput(),
			'paid_date':DateInput(),
		}


	def __init__(self, *args, **kwargs):
		super(CommissionForm, self).__init__(*args, **kwargs)
		self.fields['event'].queryset = Event.objects.filter(status = 'COMPLETED')

class InvoiceForm(forms.ModelForm):
	""" form for Invoice"""

	helper = FormHelper()
	helper.form_tag = False
	helper.form_style = 'inline'

	class Meta:
		model = Invoice
		exclude = ['']
		widgets = {
			'generated_date':DateInput(),
			'due_date':DateInput(),
			'paid_date':DateInput(),
		}

	def __init__(self, *args, **kwargs):
		super(InvoiceForm, self).__init__(*args, **kwargs)
		self.fields['event'].queryset = Event.objects.filter(status = 'COMPLETED')


class BillForm(forms.ModelForm):
	""" form for Invoice"""

	helper = FormHelper()
	helper.form_tag = False
	helper.form_style = 'inline'

	class Meta:
		model = Bill
		exclude = ['']
		widgets = {
			'generated_date':DateInput(),
			'due_date':DateInput(),
			'paid_date':DateInput(),
		}
