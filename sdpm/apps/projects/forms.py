# -*- coding: utf-8 -*-
"""
    projects.forms
    Has the content related to forms for a project.
    
    :copyright: (c) 2012 by Arruda.
"""

from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

from projects.models import Project, ProjectMember



class NewProjectForm(forms.ModelForm):
    "new project form"
    
    
    class Meta:
        model = Project
        exclude = ('enterprise','members')
        
#    def __init__(self, enterprise, *args, **kwargs):
#        super(NewProjectForm, self).__init__(*args, **kwargs)
#        self.fields['members'].queryset = enterprise.members.all()    

class NewProjectMemberForm(forms.ModelForm):
    "new project member"
    
    class Meta:
        model = ProjectMember
    
    def __init__(self, enterprise, *args, **kwargs):
        super(NewProjectForm, self).__init__(*args, **kwargs)
        self.fields['members'].queryset = enterprise.members.all()    

#    