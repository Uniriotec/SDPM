# -*- coding: utf-8 -*-
"""
    enterprises.forms
    Has the content related to forms for an enterprise.
    
    :copyright: (c) 2012 by Arruda.
"""

from django import forms
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):
    "Form that register a enterprise and a owner user for it"
    enterprise = forms.CharField(max_length=100)
    
    owner_email = forms.EmailField(label=_("Owner's Email"))
    passowrd = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    
    
    def clean_owner_email(self):
        data = self.cleaned_data['owner_email']
        if "fred@example.com" not in data:
            raise forms.ValidationError("You have forgotten about Fred!")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data