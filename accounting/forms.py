from django import forms


from crispy_forms.helper import FormHelper

from .models import Payin

class PayinForm(forms.ModelForm):
    """ form for payins"""
    helper = FormHelper()
    helper.form_tag = False
    helper.form_style = 'inline'

    class Meta:
        model = Payin
        exclude = ['']
