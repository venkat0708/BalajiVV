from django import forms
from django.db.models import Q

from crispy_forms.helper import FormHelper

from .models import Payin, PayCommissionOrSalary, Commission, Invoice, Bill, CommissionStructure, Payout
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
		exclude =['payouts']
		widgets = {
			'generated_date':DateInput(),
			'due_date':DateInput(),
			'paid_date':DateInput(),
		}




class InvoiceForm(forms.ModelForm):
	""" form for Invoice"""

	helper = FormHelper()
	helper.form_tag = False
	helper.form_style = 'inline'

	class Meta:
		model = Invoice
		exclude = ['payins']
		widgets = {
			'generated_date':DateInput(),
			'due_date':DateInput(),
			'paid_date':DateInput(),
		}




class BillForm(forms.ModelForm):
	""" form for Invoice"""

	helper = FormHelper()
	helper.form_tag = False
	helper.form_style = 'inline'

	class Meta:
		model = Bill
		exclude = ['payouts']
		widgets = {
			'generated_date':DateInput(),
			'due_date':DateInput(),
			'paid_date':DateInput(),
		}


class CommissionStructureForm(forms.ModelForm):
	""" form for Invoice"""

	helper = FormHelper()
	helper.form_tag = False
	helper.form_style = 'inline'

	class Meta:
		model = CommissionStructure
		exclude = ['']


class PayoutForm(forms.ModelForm):
    """ form for payins"""
    helper = FormHelper()
    helper.form_tag = False
    helper.form_style = 'inline'

    class Meta:
        model = Payout
        exclude = ['']
        widgets = {
			'date' : DateInput(),
		}
