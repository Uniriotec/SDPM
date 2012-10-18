# -*- coding: utf-8 -*-
"""
    enterprises.forms
    Has the content related to forms for an enterprise.
    
    :copyright: (c) 2012 by Arruda.
"""

from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

from enterprises.models import EnterpriseMember



class RegistrationForm(forms.Form):
    "Form that register a enterprise and a owner user for it"
    enterprise = forms.CharField(label=_("Enterprise's Name"), max_length=100)
#    
    owner_email = forms.EmailField(label=_("Owner's Email"))
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput,
        help_text = _("Enter the same password as above, for verification."))
#    
#    
    def clean_owner_email(self):
        data = self.cleaned_data['owner_email']
        if User.objects.filter(email=data.lower()).count() > 0:
            raise forms.ValidationError(_("This email is already been used"))

        return data
#    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2
    
    
class NewEnterpriseMemberForm(forms.ModelForm):
    "a form to create a new member for a enterprise"
    
    member_email = forms.EmailField(label=_("Member's Email"))
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput,
        help_text = _("Enter the same password as above, for verification."))
#    
#    
    class Meta:
        model = EnterpriseMember    
        fields= ('member_type',)


#    def __init__(self, *args, **kwargs):
#        super(NewEnterpriseMemberForm, self).__init__(*args, **kwargs)
#        self.fields['enterprise'].queryset = self.instance.enterprise
        
    def clean_member_email(self):
        data = self.cleaned_data['member_email']
        if User.objects.filter(email=data.lower()).count() > 0:
            raise forms.ValidationError(_("This email is already been used"))

        return data
#    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2
    
    
#    