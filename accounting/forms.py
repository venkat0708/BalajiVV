from django import forms
from django.db.models import Q

from crispy_forms.helper import FormHelper

from .models import Payin, PayCommissionOrSalary
from booking.models import Event

class PayinForm(forms.ModelForm):
    """ form for payins"""
    helper = FormHelper()
    helper.form_tag = False
    helper.form_style = 'inline'

    class Meta:
        model = Payin
        exclude = ['']

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
