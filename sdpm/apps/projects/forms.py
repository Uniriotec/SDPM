# -*- coding: utf-8 -*-
"""
    projects.forms
    Has the content related to forms for a project.
    
    :copyright: (c) 2012 by Arruda.
"""

from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from model_utils import Choices


from projects.models import Project,  Task



class NewProjectForm(forms.ModelForm):
    "new project form"
    
    
    class Meta:
        model = Project
        exclude = ('enterprise',)#'members')
        
    def __init__(self, enterprise, *args, **kwargs):
        super(NewProjectForm, self).__init__(*args, **kwargs)
        self.fields['members'].queryset = enterprise.members.all()    
#
#class NewProjectMemberForm(forms.ModelForm):
#    "new project member"
#    
#    class Meta:
#        model = ProjectMember
#    
#    def __init__(self, enterprise, *args, **kwargs):
#        super(NewProjectForm, self).__init__(*args, **kwargs)
#        self.fields['members'].queryset = enterprise.members.all()    

#    

class NewTaskForm(forms.ModelForm):
    "new task"
    
    class Meta:
        model = Task
        exclude = ('project',)
    
    def __init__(self, project, *args, **kwargs):
        super(NewTaskForm, self).__init__(*args, **kwargs)
        self.fields['assigned'].queryset = project.enterprise.members.all()    


class TaskFilterForm(forms.Form):
    "filters parameters for tasks"
    
    ORDER_CHOICES = (
        ('points', _('Points')),
        ('start_date', _('Start Date')),
        ('end_date', _('End Date')),
        ('status',  _('Status')),
        ('project',  _('Project')),
    )
    
    TASK_STATUS_WITH_BLANK=[('','---------'),] + [(k,v.__unicode__()) for k,v in Task.STATUS] 
    
    order = forms.ChoiceField(label=_('Order by'), choices=ORDER_CHOICES,initial='points', required=False)
    owner = forms.BooleanField(label=_('Owned by you'), required=False)
    status = forms.ChoiceField(label=_('Status'), choices=TASK_STATUS_WITH_BLANK ,initial='', required=False)
    
    def __init__(self, member, *args, **kwargs):
        self.member = member
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        
        self.fields['project'] = forms.ModelChoiceField(label=_('Project'), queryset=self.member.enterprise.projects.all(),  required=False)
        

    def get_tasks(self):
        "return the tasks based upon this form data"
        
        tasks = Task.objects.filter(project__in=self.member.enterprise.projects.all()).order_by('points')
        
        #get order
        order_by = self.cleaned_data.get('order',None)
        if order_by:
            tasks = tasks.order_by(order_by)
            
        project = self.cleaned_data.get('project',None)        
        if project:
            tasks = tasks.filter(project=project)
    
        owner = self.cleaned_data.get('owner',None)
        if owner:
            tasks = tasks.filter(assigned=self.member)
    
        status = self.cleaned_data.get('status',None)
        if status:
            tasks = tasks.filter(status=status)
            
        return tasks